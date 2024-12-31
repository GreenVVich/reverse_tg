from dataclasses import dataclass

CASES = ['nominative', 'genitive', 'dative', 'accusative', 'instrumental', 'prepositional']
BLOCK_TYPES = ['str', 'char', 'act', 'line', 'user']


@dataclass
class Block:
    type: int
    applying_set: list[int] | None = None
    word: str | None = None


@dataclass
class Char:
    words: list[str]

    def __getitem__(self, index: int) -> str:
        return self.words[index]


@dataclass
class Act:
    word: str
    case: int


@dataclass
class Line:
    word: str


@dataclass
class Rules:  # TODO Tags
    story_line: list[Block]
    chars: list[Char] | None = None
    acts: list[Act] | None = None
    lines: list[Line] | None = None
