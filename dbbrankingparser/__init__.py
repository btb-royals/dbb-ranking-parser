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
from .http import assemble_url, fetch_content


def load_ranking_for_league(league_id):
    """Fetch the HTML ranking for that league and yield ranks extracted
    from it.
    """
    url = assemble_url(league_id)
    return load_ranking_from_url(url)


def load_ranking_from_url(url):
    """Fetch the URL's content and yield ranks extracted from it."""
    html = fetch_content(url)
    return parse(html)
