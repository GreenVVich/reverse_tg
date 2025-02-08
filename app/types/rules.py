from dataclasses import dataclass


@dataclass
class Block:
    label: str
    applying_set: list[int] | None = None


@dataclass
class Set:
    set: list[str]

    def __getitem__(self, index: int) -> str:
        return self.set[index]

    def __len__(self) -> int:
        return len(self.set)


@dataclass
class Rules:  # TODO Tags
    story_line: list[Block]  # TODO New vision of storyline
    labels: list[str]
    sets: dict[str, Set]
