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

from functools import partial
from urllib.request import Request, urlopen

from lxml.html import document_fromstring


USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) ' \
             'Gecko/20100101 Firefox/38.0 Iceweasel/38.6.0'


def load_ranking(url):
    """Fetch the content of the URL and parse it."""
    request_headers = {'User-Agent': USER_AGENT}
    request = Request(url, headers=request_headers)

    response_body = urlopen(request).read().decode('utf-8')

    return parse(response_body)


def parse(html):
    """Extract ranking data from HTML document."""
    root = document_fromstring(html)

    # Find all table rows with team and ranking data.
    trs = root.xpath(
        'body/form/table[@class="sportView"][2]/tr[position() > 1]')

    # Fetch row cells' contents.
    ranks = map(_parse_rank, trs)
    return list(filter(None, ranks))


def _parse_rank(tr):
    """Extract a single ranking from a table row."""
    withdrawn = _is_team_withdrawn(tr)

    xpath_expression = 'td/nobr/strike/text()' if withdrawn \
                       else 'td/nobr/text()'

    values = tr.xpath(xpath_expression)

    if not values:
        return None

    attributes = _convert_attributes(values)
    attributes['withdrawn'] = withdrawn
    return attributes


def _is_team_withdrawn(tr):
    """Return `True` if the markup indicates that the team has withdrawn."""
    return bool(tr.xpath('td[2]/nobr/strike'))


def _convert_attributes(values):
    """Convert values using a predefined function.

    Return a dictionary.
    """
    return {name: converter(value)
            for (name, converter), value
            in zip(ATTRIBUTES, values)}


def intpair_factory(separator):
    return partial(intpair, separator=separator)


def intpair(value, separator):
    return tuple(map(int, value.split(separator, 1)))


ATTRIBUTES = (
    ('rank', int),
    ('name', str),
    ('games', int),
    ('wonlost', intpair_factory('/')),
    ('points', int),
    ('baskets', intpair_factory(':')),
    ('difference', int),
)
