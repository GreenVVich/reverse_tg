from typing import Dict

from managers.regulator import regulator
from managers.rule import Rules
from utils.helpers import rand_sel


class Generator:
    rules: Rules = regulator.get_rules()
    story: str = ''

    def make_code(self) -> str:
        code = (rand_sel(self.rules.actors) + rand_sel(self.rules.first_action) + rand_sel(self.rules.actors) +
                rand_sel(self.rules.second_action) + rand_sel(self.rules.actors))
        return code

    def run(self, in_code=None) -> str:
        if in_code:
            code = in_code
        else:
            code = self.make_code()
        story = (f'{self.rules.actors[int(code[0]) - 1][0]} '
                 f'{self.rules.first_action[int(code[1]) - 1].word} '
                 f'{self.rules.actors[int(code[2]) - 1][self.rules.first_action[int(code[1]) - 1].case]} '
                 f'{self.rules.second_action[int(code[3]) - 1].word} '
                 f'{self.rules.actors[int(code[4]) - 1][self.rules.second_action[int(code[3]) - 1].case]}')
        return story[0].upper() + story[1:]


generator = Generator()

if __name__ == '__main__':
    print(generator.run('21113'))
