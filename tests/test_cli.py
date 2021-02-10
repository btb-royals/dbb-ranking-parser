"""
:Copyright: 2006-2021 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from io import StringIO

import pytest

from dbbrankingparser.cli import main


def test_main_without_args_fails():
    args = []

    with pytest.raises(SystemExit):
        run_main(args)


def test_main_with_non_integer_league_id_fails():
    args = ['foo']

    with pytest.raises(SystemExit):
        run_main(args)


def test_main_with_valid_league_id_succeeds():
    args = ['12345']

    output = run_main(args)

    assert output == '[{"rank": 1}]'


# helpers


def run_main(args):
    fp = StringIO()
    faked_result = [{'rank': 1}]

    main(args=args, fp=fp, faked_result=faked_result)

    return fp.getvalue()
