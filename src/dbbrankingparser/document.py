"""
dbbrankingparser.document
~~~~~~~~~~~~~~~~~~~~~~~~~

HTML document utilities

:Copyright: 2006-2021 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from typing import Any, Dict, Iterator, List, Optional

from lxml.html import document_fromstring, HtmlElement

from .conversion import convert_attributes


def parse(html: str) -> List[Dict[str, Any]]:
    """Yield ranks extracted from HTML document."""
    trs = _select_rank_rows(html)
    return list(_parse_rank_rows(trs))


def _select_rank_rows(html: str) -> List[HtmlElement]:
    """Return the table rows that are expected to contain rank data."""
    root = document_fromstring(html)
    return root.xpath(
        'body/form/table[@class="sportView"][2]/tr[position() > 1]'
    )


def _parse_rank_rows(trs: List[HtmlElement]) -> Iterator[Dict[str, Any]]:
    """Yield ranks extracted from table rows."""
    for tr in trs:
        rank = _parse_rank_row(tr)
        if rank:
            yield rank


def _parse_rank_row(tr: HtmlElement) -> Optional[Dict[str, Any]]:
    """Attempt to extract a single rank's properties from a table row."""
    team_has_withdrawn = _has_team_withdrawn(tr)

    values = _get_rank_values(tr, team_has_withdrawn)
    if not values:
        return None

    attributes = convert_attributes(values)
    attributes['withdrawn'] = team_has_withdrawn
    return attributes


def _has_team_withdrawn(tr: HtmlElement) -> bool:
    """Return `True` if the markup indicates that the team has withdrawn."""
    return bool(tr.xpath('td[2]/nobr/strike'))


def _get_rank_values(tr: HtmlElement, team_has_withdrawn: bool) -> List[str]:
    """Return that row's cell values."""
    xpath_expression = (
        'td/nobr/strike/text()' if team_has_withdrawn else 'td/nobr/text()'
    )

    return tr.xpath(xpath_expression)
