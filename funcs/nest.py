from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Nest:
    name: str
    eggs: list[Nest]
