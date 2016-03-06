# -*- coding: utf-8 -*-

"""
dbbrankingparser.http
~~~~~~~~~~~~~~~~~~~~~

HTTP utilities

:Copyright: 2006-2016 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from urllib.request import Request, urlopen


USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) ' \
             'Gecko/20100101 Firefox/38.0 Iceweasel/38.6.0'


def fetch_content(url):
    """Retrieve and return the content of that URL."""
    request = create_request(url)
    return urlopen(request).read().decode('utf-8')


def create_request(url):
    """Create an HTTP GET request."""
    headers = {'User-Agent': USER_AGENT}
    return Request(url, headers=headers)
