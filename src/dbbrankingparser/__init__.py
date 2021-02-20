"""
DBB Ranking Parser
~~~~~~~~~~~~~~~~~~

Extract league rankings from the DBB (Deutscher Basketball Bund e.V.)
website.

The resulting data is structured as a list of dictionaries.

Please note that rankings are usually only available for the current
season, but not those of the past.

:Copyright: 2006-2021 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from .main import load_ranking_for_league, load_ranking_from_url


VERSION = '0.4.2'
