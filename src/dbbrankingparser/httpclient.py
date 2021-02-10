"""
dbbrankingparser.httpclient
~~~~~~~~~~~~~~~~~~~~~~~~~~~

HTTP client utilities

:Copyright: 2006-2021 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from urllib.request import Request, urlopen


USER_AGENT: str = (
    'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
)


def assemble_url(league_id: int) -> str:
    """Assemble the ranking HTML's URL for the league with that ID."""
    template = (
        'http://www.basketball-bund.net/public/tabelle.jsp'
        '?print=1'
        '&viewDescKey=sport.dbb.views.TabellePublicView/index.jsp_'
        '&liga_id={:d}'
    )

    return template.format(league_id)


def fetch_content(url: str) -> str:
    """Retrieve and return the content of that URL."""
    request = _create_request(url)
    return urlopen(request).read().decode('utf-8')


def _create_request(url: str) -> Request:
    """Create an HTTP GET request."""
    headers = {'User-Agent': USER_AGENT}
    return Request(url, headers=headers)
