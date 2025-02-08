from random import choice, randint

from app.managers.regulator import regulator


class Generator:  # TODO convert to one method

    @staticmethod
    def run(selected_rule: int = 0) -> str:
        rules = regulator.get_rules(selected_rule)
        story = ''
        for block in rules.story_line:
            if block.applying_set:
                selected = choice(block.applying_set)
            else:
                selected = choice(range(len(rules.sets[block.label])))
            story += rules.sets[block.label][selected]

        return story[0].upper() + story[1:]  # TODO validation+fixing with api / lib

    @staticmethod
    def random_rule() -> int:
        return randint(0, len(regulator.rules) - 1)


generator = Generator()

if __name__ == '__main__':
    for _ in range(1):
        print(generator.run())
