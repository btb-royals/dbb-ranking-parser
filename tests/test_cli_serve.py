"""
:Copyright: 2006-2021 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

import pytest

from dbbrankingparser.cli import parse_args


def test_serve_defaults():
    actual = parse_args(['serve'])

    assert actual.host == '127.0.0.1'
    assert actual.port == 8080


def test_serve_custom_host():
    actual = parse_args(['serve', '--host', '0.0.0.0'])

    assert actual.host == '0.0.0.0'
    assert actual.port == 8080


def test_serve_custom_port():
    actual = parse_args(['serve', '--port', '80'])

    assert actual.host == '127.0.0.1'
    assert actual.port == 80


def test_serve_custom_host_and_port():
    actual = parse_args(['serve', '--host', '10.10.4.22', '--port', '8092'])

    assert actual.host == '10.10.4.22'
    assert actual.port == 8092
