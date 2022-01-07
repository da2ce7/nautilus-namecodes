"""Dataclass for the Data Encoded into a Namecode Filename"""

from dataclasses import dataclass, field
from typing import Iterable, List, Literal, NamedTuple, Optional, Tuple, Union


@dataclass
class NameCode:
    code: int
    name: str


@dataclass
class LibraryCode:
    library_code: str


@dataclass
class ItemCode:
    item_code: int


@dataclass
class Listing:
    edition: NameCode
    revision: NameCode


@dataclass
class BaseVairant:
    modifications: List[NameCode]


@dataclass
class Base:
    literal: Literal["clean"]
    vairant: Optional[BaseVairant] = None


@dataclass
class GoldAlternative:
    modifications: List[NameCode]
    base: Optional[Base]


@dataclass
class Gold:
    literal: Literal["original"]
    alternative: Optional[GoldAlternative] = None
    base: Optional[Optional[Base]] = None


@dataclass
class Filename:
    library: LibraryCode
    item: ItemCode
    info: Gold
