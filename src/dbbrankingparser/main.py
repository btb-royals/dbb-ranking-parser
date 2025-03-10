"""
dbbrankingparser.main
~~~~~~~~~~~~~~~~~~~~~

Main entry point

:Copyright: 2006-2025 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from typing import Any

from .document import parse
from .httpclient import assemble_url, fetch_content


def load_ranking_for_league(league_id: int) -> list[dict[str, Any]]:
    """Fetch the HTML ranking for that league and yield ranks extracted
    from it.
    """
    url = assemble_url(league_id)
    return load_ranking_from_url(url)


def load_ranking_from_url(url: str) -> list[dict[str, Any]]:
    """Fetch the URL's content and yield ranks extracted from it."""
    html = fetch_content(url)
    return parse(html)
