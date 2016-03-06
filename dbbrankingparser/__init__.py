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

from .document import parse
from .http import fetch_content


def load_ranking(url):
    """Fetch the URL's content and yield ranks extracted from it."""
    html = fetch_content(url)
    return parse(html)
