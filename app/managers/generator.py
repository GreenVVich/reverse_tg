from random import choice

from app.managers.regulator import regulator
from app.types.rules import Rules, BLOCK_TYPES


class Generator:
    selected_rule: int = 0
    rules: Rules = regulator.get_rules(selected_rule)

    def run(self, rules: Rules = None) -> str:
        if not rules:
            rules = self.rules
        story = ''
        char_case = 0
        for block in rules.story_line:
            if BLOCK_TYPES[block.type] == 'str':
                story += block.word

            elif BLOCK_TYPES[block.type] == 'char':
                story += rules.chars[choice(block.applying_set) - 1][char_case]
                char_case = 0

            elif BLOCK_TYPES[block.type] == 'act':
                selected_act = choice(block.applying_set) - 1
                char_case = rules.acts[selected_act].case
                story += rules.acts[selected_act].word

            elif BLOCK_TYPES[block.type] == 'line':
                story += choice(rules.lines)
                # TODO New Types

            else:
                ...  # TODO Error message
        return story[0].upper() + story[1:]  # TODO validation+fixing with api / lib


generator = Generator()

if __name__ == '__main__':
    for _ in range(5):
        print(generator.run())
