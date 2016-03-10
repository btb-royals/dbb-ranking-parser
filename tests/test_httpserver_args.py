# -*- coding: utf-8 -*-

"""
:Copyright: 2006-2016 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

import unittest

from dbbrankingparser.httpserver import parse_args


class ParseArgsTest(unittest.TestCase):

    def test_defaults(self):
        actual = parse_args([])

        self.assertEqual(actual.host, '127.0.0.1')
        self.assertEqual(actual.port, 8080)

    def test_custom_host(self):
        actual = parse_args(['--host', '0.0.0.0'])

        self.assertEqual(actual.host, '0.0.0.0')
        self.assertEqual(actual.port, 8080)

    def test_custom_port(self):
        actual = parse_args(['--port', '80'])

        self.assertEqual(actual.host, '127.0.0.1')
        self.assertEqual(actual.port, 80)

    def test_custom_host_and_port(self):
        actual = parse_args(['--host', '10.10.4.22', '--port', '8092'])

        self.assertEqual(actual.host, '10.10.4.22')
        self.assertEqual(actual.port, 8092)
