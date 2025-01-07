"""
dbbrankingparser.conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Conversion of extracted values into a structure of named values of the
appropriate type.

:Copyright: 2006-2024 Jochen Kupperschmidt
:License: MIT, see LICENSE for details.
"""

from functools import partial
from typing import Any, Callable, cast, Iterable


def intpair_factory(separator: str) -> Callable[[str], tuple[int, int]]:
    return partial(intpair, separator=separator)


def intpair(value: str, separator: str) -> tuple[int, int]:
    pair = tuple(map(int, value.split(separator, maxsplit=1)))
    return cast(tuple[int, int], pair)


ATTRIBUTES: list[tuple[str, Callable[[str], Any]]] = [
    ('rank', int),
    ('name', str),
    ('games', int),
    ('wonlost', intpair_factory('/')),
    ('points', int),
    ('baskets', intpair_factory(':')),
    ('difference', int),
]


def convert_attributes(values: Iterable[str]) -> dict[str, Any]:
    """Type-convert and name rank attribute values."""
    return {
        name: converter(value)
        for (name, converter), value in zip(ATTRIBUTES, values)
    }
