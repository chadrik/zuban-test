from __future__ import absolute_import, print_function

import typing

from typing import Protocol

@typing.runtime_checkable
class Validatable(Protocol):
    def validate(self) -> dict:
        pass


class Concrete:
    def priority(self) -> int:
        return 1

    def validate(self) -> dict:
        return {}


def thing(arg: Concrete | str) -> None:
    if isinstance(arg, Validatable):
        arg.priority()
        arg.validate()
