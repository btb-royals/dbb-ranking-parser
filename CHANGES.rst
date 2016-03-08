DBB Ranking Parser Changelog
============================


Version 0.3
-----------

not yet released

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
