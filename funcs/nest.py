from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Nest:
    # id should be unique such that any nest can
    # be referenced by it
    id: int
    # Name of the task that we are trying to complete
    name: str
    done: bool

    parent: int
    children: list

    def add_child(self, id: int):
        self.children += [id]

    def remove_child(self, id: int):
        self.children.remove(id)
