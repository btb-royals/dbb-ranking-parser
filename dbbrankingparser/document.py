"""
dbbrankingparser.document
~~~~~~~~~~~~~~~~~~~~~~~~~

HTML document utilities

:Copyright: 2006-2021 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from lxml.html import document_fromstring

from .conversion import convert_attributes


def parse(html):
    """Yield ranks extracted from HTML document."""
    trs = select_rank_rows(html)
    return parse_rank_rows(trs)


def select_rank_rows(html):
    """Return the table rows that are expected to contain rank data."""
    root = document_fromstring(html)
    return root.xpath(
        'body/form/table[@class="sportView"][2]/tr[position() > 1]')


def parse_rank_rows(trs):
    """Yield ranks extracted from table rows."""
    for tr in trs:
        rank = parse_rank_row(tr)
        if rank:
            yield rank


def parse_rank_row(tr):
    """Attempt to extract a single rank's properties from a table row."""
    team_has_withdrawn = has_team_withdrawn(tr)

    values = get_rank_values(tr, team_has_withdrawn)

    if not values:
        return None

    attributes = convert_attributes(values)
    attributes['withdrawn'] = team_has_withdrawn
    return attributes


def has_team_withdrawn(tr):
    """Return `True` if the markup indicates that the team has withdrawn."""
    return bool(tr.xpath('td[2]/nobr/strike'))


def get_rank_values(tr, team_has_withdrawn):
    """Return that row's cell values."""
    xpath_expression = 'td/nobr/strike/text()' if team_has_withdrawn \
                       else 'td/nobr/text()'

    return tr.xpath(xpath_expression)
