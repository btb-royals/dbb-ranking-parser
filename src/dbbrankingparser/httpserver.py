"""
dbbrankingparser.httpserver
~~~~~~~~~~~~~~~~~~~~~~~~~~~

HTTP server to forward requests to the parser and return the result as
JSON.

Expected request URL path: `/<league id>`, e.g. `/12345`. Raises 404 on
invalid league id.

:Copyright: 2006-2021 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from typing import Optional
from urllib.parse import urlsplit

from .main import load_ranking_for_league


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self) -> None:
        league_id = self.extract_league_id_from_path()

        if league_id is None:
            self.send_response_only(404, message='')
            self.end_headers()
            return

        ranking = list(load_ranking_for_league(league_id))
        ranking_json = json.dumps(ranking).encode('utf-8')

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(ranking_json)

    def version_string(self) -> str:
        return 'DBB Ranking Parser'

    def extract_league_id_from_path(self) -> Optional[int]:
        value = urlsplit(self.path).path.lstrip('/')

        try:
            return int(value)
        except ValueError:
            return None


def serve(host: str, port: int) -> None:
    """Serve HTTP requests."""
    address = (host, port)

    server = HTTPServer(address, RequestHandler)
    print('Listening for HTTP requests on {}:{:d} ...'.format(*address))
    server.serve_forever()
