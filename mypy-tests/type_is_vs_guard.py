from __future__ import absolute_import, print_function

from typing import Iterable, TypeVar, TypeGuard, overload, Iterator, Union, Hashable
from typing_extensions import TypeIs, reveal_type

T = TypeVar("T")

#
# @overload
# def is_iterable(x: Iterable[T]) -> TypeIs[Iterable[T]]:
#     pass

def is_iterable(x: object) -> TypeGuard[Iterable]:
    pass


def test1() -> None:
    x = ["one", "two"]
    if is_iterable(x):
        reveal_type(x)
    else:
        reveal_type(x)

def test2() -> None:
    x = "one"
    if is_iterable(x):
        reveal_type(x)
    else:
        reveal_type(x)


def _iter_values(value: Union[Hashable, Iterable[Hashable]]) -> Iterator[Hashable]:
    if is_iterable(value):
        reveal_type(value)
        yield from value
    else:
        # TYPING: `value` is Hashable, but `is_iterable` is not
        #  error: Incompatible types in "yield" (actual type "Union[Hashable,
        #  Iterable[Hashable]]", expected type "Hashable")  [misc]
        reveal_type(value)
        yield value
