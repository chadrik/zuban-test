from typing import TYPE_CHECKING

class Foo:
    def __init__(self, name: str):
        self.name: str = name
        if TYPE_CHECKING:
            reveal_type(self.name)

