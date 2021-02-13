"""
:Copyright: 2006-2021 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from io import StringIO

import pytest

from dbbrankingparser.cli import main


def test_get_without_args_fails():
    args = ['get']

    with pytest.raises(SystemExit):
        run_get(args)


def test_get_with_non_integer_league_id_fails():
    args = ['get', 'foo']

    with pytest.raises(SystemExit):
        run_get(args)


def test_get_with_valid_league_id_succeeds():
    args = ['get', '12345']

    output = run_get(args)

    assert output == '[{"rank": 1}]'


# helpers


def run_get(args):
    fp = StringIO()
    faked_result = [{'rank': 1}]

    main(args=args, fp=fp, faked_result=faked_result)

    return fp.getvalue()
