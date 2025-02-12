from app.types.rules import Rules, ShortRule
from rules import RULE_BOOK


class Regulator:
    rules: list[Rules] = RULE_BOOK

    def get_rules(self, selected_rule: int = 0) -> Rules:
        return self.rules[selected_rule]

    def update_rules(self) -> None:
        ...  # TODO

    def get_rule_list(self) -> list[ShortRule]:
        result = []
        for i, rule in enumerate(self.rules):
            result.append(ShortRule(i, rule.name))
        return result


regulator = Regulator()

if __name__ == '__main__':
    print(regulator.get_rules())
