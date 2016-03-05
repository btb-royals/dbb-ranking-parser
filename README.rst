DBB Ranking Parser
==================

Extract league rankings from the DBB_ (Deutscher Basketball Bund e.V.)
website.

This library has been extracted from the web application behind the
website of the `BTB Royals Oldenburg`_ (a basketball team from
Oldenburg, Germany) where it has proven itself for many, many years.


Requirements
------------

- Python_ 3.4+
- lxml_


Installation
------------

Install this package via pip_:

.. code:: sh

    $ pip install dbbrankingparser

Because of the dependency on lxml_, this will also require the header
files for the targeted Python_ version as well as those for libxml2_ and
libxslt_.

On `Debian Linux`_, one should be able to install these from the
distribution's repositories (as the 'root' user):

.. code:: sh

    # aptitude update
    # aptitude install python3.4-dev libxml2-dev libxslt1-dev

Apart from that (for example, if those packages are not yet installed)
it might be easier to install Debian's pre-built binary packages for
lxml_ instead:

.. code:: sh

    # aptitude update
    # aptitude install python-lxml


Usage
-----

To fetch and parse a league ranking, the appropriate URL is required.

It can be obtained on the DBB_ website. On every league's ranking page
there should be a link to a (non-"XL") HTML print version.

Its target URL should look like this (assuming the league's ID is
12345):
``http://www.basketball-bund.net/public/tabelle.jsp?print=1&viewDescKey=sport.dbb.views.TabellePublicView/index.jsp_&liga_id=12345``

.. code:: python

    from dbbrankingparser import load_ranking


    URL = '<see example above>'

    ranking = load_ranking(URL)

    top_team = ranking[0]
    print('Top team:', top_team['name'])


.. _DBB:                  http://www.basketball-bund.net/
.. _BTB Royals Oldenburg: https://www.btbroyals.de/
.. _Python:               https://www.python.org/
.. _pip:                  http://www.pip-installer.org/
.. _lxml:                 http://lxml.de/
.. _libxml2:              http://xmlsoft.org/XSLT/
.. _libxslt:              http://xmlsoft.org/XSLT/
.. _Debian Linux:         https://www.debian.org/


:Copyright: 2006-2016 Jochen Kupperschmidt
:Date: 05-Mar-2016
:License: MIT, see LICENSE for details.
:Version: 0.1-dev
:Website: http://homework.nwsnet.de/releases/4a51/#dbb-ranking-parser
