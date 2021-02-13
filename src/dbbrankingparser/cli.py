"""
dbbrankingparser.cli
~~~~~~~~~~~~~~~~~~~~

Command line interface

:Copyright: 2006-2021 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from argparse import ArgumentParser
import json
import sys

from . import VERSION
from .httpserver import serve
from .main import load_ranking_for_league


def parse_args(args=None):
    """Parse command line arguments.

    The optional `args` argument allows to directly pass arguments (as a
    list of strings) to the argument parser instead of expecting them on
    the command line (i.e. `sys.argv`).
    """
    parser = _create_parser()
    return parser.parse_args(args)


def _create_parser() -> ArgumentParser:
    parser = ArgumentParser()

    parser.add_argument(
        '--version', action='version', version=f'DBB Ranking Parser {VERSION}'
    )

    subparsers = parser.add_subparsers(dest='subparser')
    _add_get_subparser(subparsers)
    _add_serve_subparser(subparsers)

    return parser


def _add_get_subparser(subparsers) -> None:
    parser = subparsers.add_parser('get')
    parser.add_argument('league_id', type=int)


def _add_serve_subparser(subparsers) -> None:
    parser = subparsers.add_parser('serve')

    default_host = '127.0.0.1'
    parser.add_argument(
        '--host',
        default=default_host,
        help='the host to listen on [default: {}]'.format(default_host),
    )

    default_port = 8080
    parser.add_argument(
        '--port',
        type=int,
        default=default_port,
        help='the port to listen on [default: {:d}]'.format(default_port),
    )


def main(*, args=None, fp=sys.stdout, faked_result=None) -> None:
    """Entry point for command line script."""
    args = parse_args(args)

    if args.subparser == 'get':
        _run_get(args, fp, faked_result)
    elif args.subparser == 'serve':
        _run_serve(args)


def _run_get(args, fp, faked_result=None) -> None:
    """Require a league ID on the command line and write the
    corresponding ranking as JSON to STDOUT.
    """
    if faked_result is None:
        ranking = list(load_ranking_for_league(args.league_id))
    else:
        ranking = faked_result

    json.dump(ranking, fp)


def _run_serve(args) -> None:
    """Run HTTP server."""
    serve(args.host, args.port)
