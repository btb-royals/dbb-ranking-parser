# -*- coding: utf-8 -*-

"""
dbbrankingparser.cli
~~~~~~~~~~~~~~~~~~~~

Command line interface

:Copyright: 2006-2016 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from argparse import ArgumentParser
import json
import sys

from .main import load_ranking_for_league


def create_arg_parser():
    """Prepare the command line arguments parser."""
    parser = ArgumentParser()

    parser.add_argument('league_id', type=int)

    return parser


def parse_args(args=None):
    """Parse command line arguments.

    The optional `args` argument allows to directly pass arguments (as a
    list of strings) to the argument parser instead of expecting them on
    the command line (i.e. `sys.argv`).
    """
    parser = create_arg_parser()
    return parser.parse_args(args)


def main(*, args=None, fp=sys.stdout, faked_result=None):
    """Require a league ID on the command line and write the
    corresponding ranking as JSON to STDOUT.
    """
    args = parse_args(args)

    if faked_result is None:
        ranking = list(load_ranking_for_league(args.league_id))
    else:
        ranking = faked_result

    json.dump(ranking, fp)
