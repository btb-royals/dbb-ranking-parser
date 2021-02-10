"""
:Copyright: 2006-2021 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

import pytest

from dbbrankingparser.httpclient import assemble_url


def test_assemble_url_with_none_id():
    league_id = None

    with pytest.raises(TypeError):
        assemble_url(league_id)


def test_assemble_url_with_non_integer_id():
    league_id = 'NaN'

    with pytest.raises(ValueError):
        assemble_url(league_id)


def test_assemble_url_with_valid_id():
    league_id = 23042
    expected = 'http://www.basketball-bund.net/public/tabelle.jsp?print=1&viewDescKey=sport.dbb.views.TabellePublicView/index.jsp_&liga_id=23042'

    actual = assemble_url(league_id)

    assert actual == expected
