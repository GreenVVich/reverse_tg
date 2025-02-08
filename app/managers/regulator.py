from app.types.rules import Rules
from rules import RULE_BOOK


class Regulator:
    rules: list[Rules] = RULE_BOOK

    def get_rules(self, selected_rule: int = 0) -> Rules:
        return self.rules[selected_rule]

    def update_rules(self) -> None:
        ...  # TODO


regulator = Regulator()

if __name__ == '__main__':
    print(regulator.get_rules())
