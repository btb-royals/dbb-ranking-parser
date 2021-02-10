DBB Ranking Parser Changelog
============================


Version 0.4
-------------

Unreleased

- Added support for Python 3.6, 3.7, 3.8, and 3.9.
- Dropped support for Python 3.4.
- Updated lxml to at least version 4.6.2.
- Moved package metadata from ``setup.py`` to ``setup.cfg``.
- Switched to a ``src/`` project layout.


Version 0.3.1
-------------

Released March 10, 2016

- Allowed to specify the HTTP server's host and port on the command
  line.
- Fixed `Dockerfile` for the HTTP server to bind it to a public address
  instead of localhost so that `EXPOSE`ing it actually works.


Version 0.3
-----------

Released March 8, 2016

- Added HTTP server that wraps the parser and responds with rankings as
  JSON.
- Added `Dockerfile`s for the command line script and the HTTP server.


Version 0.2
-----------

Released March 6, 2016

- It is now sufficient to specify just the league ID instead of the full
  URL. The latter is still possible, though.
- Added a command line script to retrieve a league's ranking as JSON.
- Return nothing when parsing irrelevant HTML table rows.
- Return extracted ranks as a generator instead of a list.
- Split code over several modules.


Version 0.1
-----------

Released March 5, 2016

- first official release
