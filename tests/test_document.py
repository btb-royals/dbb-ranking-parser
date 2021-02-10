"""
:Copyright: 2006-2021 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

import pytest

from dbbrankingparser.document import parse


def test_parse_empty_ranking():
    html = """\
        <html>
          <body>

            <form>

              <table class="sportView">
              </table>

              <table class="sportView">
                <tr>
                  <td class="sportViewHeader" colspan="7"></td>
                </tr>
                <tr>
                  <td class="sportItemEven" colspan="7">Keine Einträge gefunden!</td>
                </tr>
              </table>

            </form>

          </body>
        </html>
        """

    actual = parse(html)
    assert list(actual) == []


def test_parse_valid_ranking():
    actual = parse(HTML)
    assert list(actual) == EXPECTED


EXPECTED = [
    {
        'baskets': (1815, 1391),
        'difference': 424,
        'games': 21,
        'name': 'Bürgerfelder TB',
        'points': 38,
        'rank': 1,
        'wonlost': (19, 2),
        'withdrawn': False,
    },
    {
        'baskets': (1633, 1502),
        'difference': 131,
        'games': 20,
        'name': 'TSG Westerstede',
        'points': 30,
        'rank': 2,
        'wonlost': (15, 5),
        'withdrawn': False,
    },
    {
        'baskets': (1821, 1699),
        'difference': 122,
        'games': 21,
        'name': 'TuS Red Devils Bramsche',
        'points': 28,
        'rank': 3,
        'wonlost': (14, 7),
        'withdrawn': False,
    },
    {
        'baskets': (1729, 1642),
        'difference': 87,
        'games': 21,
        'name': 'BTS Neustadt',
        'points': 26,
        'rank': 4,
        'wonlost': (13, 8),
        'withdrawn': False,
    },
    {
        'baskets': (1654, 1711),
        'difference': -57,
        'games': 21,
        'name': 'TSV Neustadt',
        'points': 24,
        'rank': 5,
        'wonlost': (12, 9),
        'withdrawn': False,
    },
    {
        'baskets': (1517, 1529),
        'difference': -12,
        'games': 20,
        'name': 'TK Hannover',
        'points': 20,
        'rank': 6,
        'wonlost': (10, 10),
        'withdrawn': False,
    },
    {
        'baskets': (1629, 1564),
        'difference': 65,
        'games': 21,
        'name': 'BasketsAkademie WE/Oldenburger TB 2',
        'points': 20,
        'rank': 7,
        'wonlost': (10, 11),
        'withdrawn': False,
    },
    {
        'baskets': (1542, 1702),
        'difference': -160,
        'games': 21,
        'name': 'VfL Hameln',
        'points': 18,
        'rank': 8,
        'wonlost': (9, 12),
        'withdrawn': False,
    },
    {
        'baskets': (1745, 1910),
        'difference': -165,
        'games': 21,
        'name': 'TV Delmenhorst',
        'points': 16,
        'rank': 9,
        'wonlost': (8, 13),
        'withdrawn': False,
    },
    {
        'baskets': (1577, 1696),
        'difference': -119,
        'games': 21,
        'name': 'Basketball Lesum Vegesack',
        'points': 14,
        'rank': 10,
        'wonlost': (7, 14),
        'withdrawn': False,
    },
    {
        'baskets': (1443, 1565),
        'difference': -122,
        'games': 21,
        'name': 'MTV/BG Wolfenbüttel',
        'points': 10,
        'rank': 11,
        'wonlost': (5, 16),
        'withdrawn': False,
    },
    {
        'baskets': (1547, 1741),
        'difference': -194,
        'games': 21,
        'name': 'BG 74 Göttingen',
        'points': 6,
        'rank': 12,
        'wonlost': (3, 18),
        'withdrawn': False,
    },
    {
        'baskets': (0, 0),
        'difference': 0,
        'games': 0,
        'name': 'UBC Hannover',
        'points': 0,
        'rank': 13,
        'wonlost': (0, 0),
        'withdrawn': True,
    },
]

# The following HTML content has been obtained from the DBB website.
HTML = """\
<html>
<head>
	<title>Deutscher Basketball-Bund e.V.</title>
	<link rel=stylesheet type="text/css" href="../dbb_print.css">
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="expires" content="0">
	<meta name="robots" content="noindex">
</head>
<body>

<table align="center">

</table>

<form name="tabelleliste" action="" method="post" >

		<table width="100%"><tr>
			<td class="print" align="left" valign="bottom">Quelle: http://basketball-bund.net</td>
			<td class="print" align="right"><img src="/images/logos/rln_logo.gif" border="0"></td></tr>
		</table>
	
<table  id="TabelleList0"  class="sportView" cellspacing="1" cellpadding="0" border="0" width="100%">
<tr>
<td>
<table cellspacing="0" cellpadding="3" border="0" width="100%">
<tr>
<td align="left" valign="top" class="sportViewTitle">Tabelle - 2.Regionalliga Herren West (Senioren; Liganr.: 3005)</td>
<td width="10" align="right" valign="top" class="sportViewTitle"><nobr>


</nobr>
</td>
</tr>
</table>
</td>
</tr>
</table>



	<!-- this code has been generated from <header> custom tag (twlist.tld) -->

<table width="100%" style="clear: left" cellpadding="0" cellspacing="1" border="0" class="sportView"><tr>
<td class="sportViewDivItem" width="40" align="center" style="text-align: center;"><table align="center"  cellspacing="0" cellpadding="0" height="100%"><tr><td class="sportViewHeader">Rang&nbsp;</td></tr></table></td>
<td class="sportViewDivItem" width="" align="center" style="text-align: center;"><table align="center"  cellspacing="0" cellpadding="0" height="100%"><tr><td class="sportViewHeader">Name&nbsp;</td></tr></table></td>
<td class="sportViewDivItem" width="60px" align="center" style="text-align: center;"><table align="center"  cellspacing="0" cellpadding="0" height="100%"><tr><td class="sportViewHeader">Spiele&nbsp;</td></tr></table></td>
<td class="sportViewDivItem" width="70px" align="center" style="text-align: center;"><table align="center"  cellspacing="0" cellpadding="0" height="100%"><tr><td class="sportViewHeader">W/L&nbsp;</td></tr></table></td>
<td class="sportViewDivItem" width="80px" align="center" style="text-align: center;"><table align="center"  cellspacing="0" cellpadding="0" height="100%"><tr><td class="sportViewHeader">Pkte&nbsp;</td></tr></table></td>
<td class="sportViewDivItem" width="80px" align="center" style="text-align: center;"><table align="center"  cellspacing="0" cellpadding="0" height="100%"><tr><td class="sportViewHeader">Körbe&nbsp;</td></tr></table></td>
<td class="sportViewDivItem" width="50px" align="center" style="text-align: center;"><table align="center"  cellspacing="0" cellpadding="0" height="100%"><tr><td class="sportViewHeader">Diff.&nbsp;</td></tr></table></td>
</tr><!-- this code has been generated from <header> custom tag (twlist.tld) -->


		<tr>

			<td class="sportItemEven" align="center"><NOBR>1<NOBR></td>
			<td class="sportItemEven"><NOBR>Bürgerfelder TB<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>21<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>19/2<NOBR></td>
			<td class="sportItemEven" align="center">
				<NOBR>
				
				38
				<NOBR>
			</td>
			<td class="sportItemEven" align="center"><NOBR>1815 : 1391<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>424<NOBR></td>
		</tr>

		<tr>

			<td class="sportItemOdd" align="center"><NOBR>2<NOBR></td>
			<td class="sportItemOdd"><NOBR>TSG Westerstede<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>20<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>15/5<NOBR></td>
			<td class="sportItemOdd" align="center">
				<NOBR>
				
				30
				<NOBR>
			</td>
			<td class="sportItemOdd" align="center"><NOBR>1633 : 1502<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>131<NOBR></td>
		</tr>

		<tr>

			<td class="sportItemEven" align="center"><NOBR>3<NOBR></td>
			<td class="sportItemEven"><NOBR>TuS Red Devils Bramsche<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>21<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>14/7<NOBR></td>
			<td class="sportItemEven" align="center">
				<NOBR>
				
				28
				<NOBR>
			</td>
			<td class="sportItemEven" align="center"><NOBR>1821 : 1699<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>122<NOBR></td>
		</tr>

		<tr>

			<td class="sportItemOdd" align="center"><NOBR>4<NOBR></td>
			<td class="sportItemOdd"><NOBR>BTS Neustadt<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>21<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>13/8<NOBR></td>
			<td class="sportItemOdd" align="center">
				<NOBR>
				
				26
				<NOBR>
			</td>
			<td class="sportItemOdd" align="center"><NOBR>1729 : 1642<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>87<NOBR></td>
		</tr>

		<tr>

			<td class="sportItemEven" align="center"><NOBR>5<NOBR></td>
			<td class="sportItemEven"><NOBR>TSV Neustadt<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>21<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>12/9<NOBR></td>
			<td class="sportItemEven" align="center">
				<NOBR>
				
				24
				<NOBR>
			</td>
			<td class="sportItemEven" align="center"><NOBR>1654 : 1711<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>-57<NOBR></td>
		</tr>

		<tr>

			<td class="sportItemOdd" align="center"><NOBR>6<NOBR></td>
			<td class="sportItemOdd"><NOBR>TK Hannover<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>20<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>10/10<NOBR></td>
			<td class="sportItemOdd" align="center">
				<NOBR>
				
				20
				<NOBR>
			</td>
			<td class="sportItemOdd" align="center"><NOBR>1517 : 1529<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>-12<NOBR></td>
		</tr>

		<tr>

			<td class="sportItemEven" align="center"><NOBR>7<NOBR></td>
			<td class="sportItemEven"><NOBR>BasketsAkademie WE/Oldenburger TB 2<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>21<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>10/11<NOBR></td>
			<td class="sportItemEven" align="center">
				<NOBR>
				
				20
				<NOBR>
			</td>
			<td class="sportItemEven" align="center"><NOBR>1629 : 1564<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>65<NOBR></td>
		</tr>

		<tr>

			<td class="sportItemOdd" align="center"><NOBR>8<NOBR></td>
			<td class="sportItemOdd"><NOBR>VfL Hameln<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>21<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>9/12<NOBR></td>
			<td class="sportItemOdd" align="center">
				<NOBR>
				
				18
				<NOBR>
			</td>
			<td class="sportItemOdd" align="center"><NOBR>1542 : 1702<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>-160<NOBR></td>
		</tr>

		<tr>

			<td class="sportItemEven" align="center"><NOBR>9<NOBR></td>
			<td class="sportItemEven"><NOBR>TV Delmenhorst<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>21<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>8/13<NOBR></td>
			<td class="sportItemEven" align="center">
				<NOBR>
				
				16
				<NOBR>
			</td>
			<td class="sportItemEven" align="center"><NOBR>1745 : 1910<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>-165<NOBR></td>
		</tr>

		<tr>

			<td class="sportItemOdd" align="center"><NOBR>10<NOBR></td>
			<td class="sportItemOdd"><NOBR>Basketball Lesum Vegesack<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>21<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>7/14<NOBR></td>
			<td class="sportItemOdd" align="center">
				<NOBR>
				
				14
				<NOBR>
			</td>
			<td class="sportItemOdd" align="center"><NOBR>1577 : 1696<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>-119<NOBR></td>
		</tr>

		<tr>

			<td class="sportItemEven" align="center"><NOBR>11<NOBR></td>
			<td class="sportItemEven"><NOBR>MTV/BG Wolfenbüttel<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>21<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>5/16<NOBR></td>
			<td class="sportItemEven" align="center">
				<NOBR>
				
				10
				<NOBR>
			</td>
			<td class="sportItemEven" align="center"><NOBR>1443 : 1565<NOBR></td>
			<td class="sportItemEven" align="center"><NOBR>-122<NOBR></td>
		</tr>

		<tr>

			<td class="sportItemOdd" align="center"><NOBR>12<NOBR></td>
			<td class="sportItemOdd"><NOBR>BG 74 Göttingen<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>21<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>3/18<NOBR></td>
			<td class="sportItemOdd" align="center">
				<NOBR>
				
				6
				<NOBR>
			</td>
			<td class="sportItemOdd" align="center"><NOBR>1547 : 1741<NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR>-194<NOBR></td>
		</tr>

		<tr>

			<td class="sportItemOdd" align="center"><NOBR><STRIKE>13</STRIKE><NOBR></td>
			<td class="sportItemOdd"><NOBR><STRIKE>UBC Hannover</STRIKE><NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR><STRIKE>0</STRIKE><NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR><STRIKE>0/0</STRIKE><NOBR></td>
			<td class="sportItemOdd" align="center">
				<NOBR>
				
				<STRIKE>0</STRIKE>
				<NOBR>
			</td>
			<td class="sportItemOdd" align="center"><NOBR><STRIKE>0 : 0</STRIKE><NOBR></td>
			<td class="sportItemOdd" align="center"><NOBR><STRIKE>0</STRIKE><NOBR></td>
		</tr>

	</table>

</form>
"""
