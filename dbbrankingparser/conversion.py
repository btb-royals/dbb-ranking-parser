# -*- coding: utf-8 -*-

"""
dbbrankingparser.conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Conversion of extracted values into a structure of named values of the
appropriate type.

:Copyright: 2006-2016 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from functools import partial


def intpair_factory(separator):
    return partial(intpair, separator=separator)


def intpair(value, separator):
    return tuple(map(int, value.split(separator, 1)))


ATTRIBUTES = [
    ('rank', int),
    ('name', str),
    ('games', int),
    ('wonlost', intpair_factory('/')),
    ('points', int),
    ('baskets', intpair_factory(':')),
    ('difference', int),
]


def convert_attributes(values):
    """Type-convert and name rank attribute values."""
    return {name: converter(value)
            for (name, converter), value
            in zip(ATTRIBUTES, values)}
