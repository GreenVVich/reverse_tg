from dataclasses import dataclass

CASES = ['nominative', 'genitive', 'dative', 'accusative', 'instrumental', 'prepositional']


@dataclass
class Actor:
    words: list[str]

    def __getitem__(self, index: int) -> str:
        return self.words[index]


@dataclass
class Action:
    word: str
    case: int


@dataclass
class Rules:
    actors: list[Actor]
    first_action: list[Action]
    second_action: list[Action]
