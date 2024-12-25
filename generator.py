from typing import Dict
from random import choice

from regulator import regulator


class Generator:
    rules: Dict[str, list[str]] = regulator.get_rules()
    case: str = ''

    def generate(self) -> str:
        case = (choice(self.rules['actors']) + choice(self.rules['first_action']) + choice(self.rules['actors']) + 'у' +
                choice(self.rules['second_action']) + choice(self.rules['actors']) + 'а')
        return case[0].upper() + case[1:]


generator = Generator()

if __name__ == '__main__':
    print(generator.generate())

