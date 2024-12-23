DBB Ranking Parser Changelog
============================


0.5.0 (unreleased)
------------------

- Added support for Python 3.10, 3.11, 3.12, and 3.13.
- Dropped support for Python 3.6, 3.7, and 3.8 (which are end-of-life).
- Updated lxml to at least version 5.3.0.
- Updated library to use HTTPS URL to fetch data.
- Moved remaining project metadata from ``setup.cfg`` to
  ``pyproject.toml``.
- Added uv lock file (``uv.lock``) to pin versions of direct and
  transitive dependencies.
- Updated Docker base image to Alpine Linux 3.21.
- Changed ``Dockerfile`` to install lxml as a Python wheel rather than
  as an Alpine package.
- Introduced virtual environment to Docker container.
- Added GitHub action to build and publish Docker images.
- Switched build backend from setuptools to Hatchling.
- Switched code formatter from Black to Ruff.


0.4.2 (2021-02-20)
------------------

- Fixed description of how to run the HTTP server in a Docker container.


0.4.1 (2021-02-13)
------------------

- Fixed reStructuredText issues in changelog which prevented a release
  on PyPI.


0.4 (2021-02-13)
----------------

- Added support for Python 3.6, 3.7, 3.8, and 3.9.
- Dropped support for Python 3.4 and 3.5 (which are end-of-life).
- Updated lxml to at least version 4.6.2.
- Moved package metadata from ``setup.py`` to ``setup.cfg``.
- Switched to a ``src/`` project layout.
- Added type hints (PEP 484).
- Ported tests from ``unittest`` to pytest.
- Merged basic and HTTP server command line interfaces into a single
  argument parser with subcommands ``get`` and ``serve``. Removed
  ``dbb-ranking-server`` entrypoint.
- Renamed command line entrypoint to ``dbb-ranking-parser``.
- Added command line option ``--version`` to show the application's
  version.
- Merged the previous three ``Dockerfile`` files into a single one.
- Updated and simplified Docker image and build process by upgrading
  Alpine Linux to 3.13 and installing lxml as a binary package,
  removing the need for local compilation.


0.3.1 (2016-03-10)
------------------

- Allowed to specify the HTTP server's host and port on the command
  line.
- Fixed ``Dockerfile`` for the HTTP server to bind it to a public address
  instead of localhost so that exposing the port actually works.


0.3 (2016-03-06)
----------------

- Added HTTP server that wraps the parser and responds with rankings as
  JSON.
- Added ``Dockerfile`` files for the command line script and the HTTP
  server.


0.2 (2016-03-06)
----------------

- It is now sufficient to specify just the league ID instead of the full
  URL. The latter is still possible, though.
- Added a command line script to retrieve a league's ranking as JSON.
- Return nothing when parsing irrelevant HTML table rows.
- Return extracted ranks as a generator instead of a list.
- Split code over several modules.


0.1 (2016-03-05)
----------------

- first official release
