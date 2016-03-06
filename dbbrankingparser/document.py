# -*- coding: utf-8 -*-

"""
dbbrankingparser.document
~~~~~~~~~~~~~~~~~~~~~~~~~

HTML document utilities

:Copyright: 2006-2016 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from lxml.html import document_fromstring


def select_rank_rows(html):
    """Return the table rows that are expected to contain rank data."""
    root = document_fromstring(html)
    return root.xpath(
        'body/form/table[@class="sportView"][2]/tr[position() > 1]')


def get_rank_values(tr, team_has_withdrawn):
    """Return that row's cell values."""
    xpath_expression = 'td/nobr/strike/text()' if team_has_withdrawn \
                       else 'td/nobr/text()'

    return tr.xpath(xpath_expression)


def has_team_withdrawn(tr):
    """Return `True` if the markup indicates that the team has withdrawn."""
    return bool(tr.xpath('td[2]/nobr/strike'))
