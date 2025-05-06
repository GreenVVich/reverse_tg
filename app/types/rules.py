from dataclasses import dataclass


@dataclass
class Block:
    label: str
    applying_set: list[int] | None = None


@dataclass
class Set:
    """
    Param
    tags: str
    combination of letters with special result modification by set
    'u' - unique (deleting used items of set)
    'r' - recursion (links to rules that will be generated in )
    """
    set: list[str]
    tags: str = ''

    def __getitem__(self, index: int) -> str:
        return self.set[index]

    def __len__(self) -> int:
        return len(self.set)

    def pop(self, index: int) -> str:
        return self.set.pop(index)


@dataclass
class Rules:  # TODO Tags
    name: str
    story_line: list[Block]
    labels: list[str]
    sets: dict[str, Set]


@dataclass
class ShortRule:
    id: int
    name: str
