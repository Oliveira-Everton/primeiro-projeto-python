from . import (
    Bag,
    Hand,
    Head
)

class Pessoa:
    def __init__(self, name=None, head=Head(), hand=Hand(), bag=Bag([])):
        self._name = name
        self._head = head
        self._hand = hand
        self._bag = bag

    @property
    def bag(self):
        return self._bag

    @property
    def head(self):
        return self._head

    @property
    def hand(self):
        return self._hand
