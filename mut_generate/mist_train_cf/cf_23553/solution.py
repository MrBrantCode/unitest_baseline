"""
QUESTION:
Implement a function `createImmutableList` that takes in a list of elements and returns an immutable list. The returned list should not be changed once it is created. The input list can contain any type of elements, including strings, integers, and other lists.
"""

from typing import TypeVar, Generic, Iterable

T = TypeVar('T')

class ImmutableList(Generic[T]):
    def __init__(self, elements: Iterable[T]):
        self._elements = tuple(elements)

    def __getitem__(self, index):
        return self._elements[index]

    def __len__(self):
        return len(self._elements)

def createImmutableList(elements: Iterable[T]) -> ImmutableList[T]:
    return ImmutableList(elements)