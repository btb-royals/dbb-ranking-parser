"""
:Copyright: 2006-2021 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from io import StringIO
import unittest

from dbbrankingparser.cli import main


class CliTest(unittest.TestCase):

    def test_main_without_args_fails(self):
        args = []

        with self.assertRaises(SystemExit):
            self.run_main(args)

    def test_main_with_non_integer_league_id_fails(self):
        args = ['foo']

        with self.assertRaises(SystemExit):
            self.run_main(args)

    def test_main_with_valid_league_id_succeeds(self):
        args = ['12345']

        output = self.run_main(args)

        self.assertEqual(output, '[{"rank": 1}]')

    # helpers

    def run_main(self, args):
        fp = StringIO()
        faked_result = [{'rank': 1}]

        main(args=args, fp=fp, faked_result=faked_result)

        return fp.getvalue()
