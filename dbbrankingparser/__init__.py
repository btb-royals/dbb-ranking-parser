# -*- coding: utf-8 -*-

"""
DBB Ranking Parser
~~~~~~~~~~~~~~~~~~

Extract league rankings from the DBB (Deutscher Basketball Bund e.V.)
website.

The resulting data is structured as a list of dictionaries.

:Copyright: 2006-2016 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from lxml.html import document_fromstring

from .conversion import convert_attributes
from .http import fetch_content


def load_ranking(url):
    """Fetch the URL's content and yield ranks extracted from it."""
    html = fetch_content(url)
    return parse(html)


def parse(html):
    """Yield ranks extracted from HTML document."""
    root = document_fromstring(html)

    trs = select_rank_rows(root)

    return _parse_rank_rows(trs)


def select_rank_rows(root):
    """Return the table rows that are expected to contain rank data."""
    return root.xpath(
        'body/form/table[@class="sportView"][2]/tr[position() > 1]')


def _parse_rank_rows(trs):
    """Yield ranks extracted from table rows."""
    for tr in trs:
        rank = _parse_rank_row(tr)
        if rank:
            yield rank


def _parse_rank_row(tr):
    """Attempt to extract a single rank's properties from a table row."""
    withdrawn = _is_team_withdrawn(tr)

    xpath_expression = 'td/nobr/strike/text()' if withdrawn \
                       else 'td/nobr/text()'

    values = tr.xpath(xpath_expression)

    if not values:
        return None

    attributes = convert_attributes(values)
    attributes['withdrawn'] = withdrawn
    return attributes


def _is_team_withdrawn(tr):
    """Return `True` if the markup indicates that the team has withdrawn."""
    return bool(tr.xpath('td[2]/nobr/strike'))
