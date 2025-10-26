from app.types.rules import Rules, ShortRule
from rules import RULE_BOOK, OPTIONAL_RULE_BOOK
from datetime import datetime


class Regulator:
    rules: list[Rules] = RULE_BOOK
    additional_rules: list[Rules] = OPTIONAL_RULE_BOOK

    def get_rules(self, selected_rule: int = 0) -> Rules:
        return self.rules[selected_rule]

    def update_rules(self) -> None:
        ...  # TODO

    def get_rule_list(self) -> list[ShortRule]:
        result = []
        counter = 0  # TODO drop after DB realization
        for i, rule in enumerate(self.rules):
            result.append(ShortRule(i, rule.name))
            counter += 1

        if datetime.now().date().month == 7 and 29 <= datetime.now().day <= 31:
            for i, rule in enumerate(self.additional_rules):
                print(1)
                if rule.name == 'Mary BD':
                    counter += 1
                    print(2)
                    result.append(ShortRule(counter, rule.name))

        if datetime.now().date().month == 1 and 5 <= datetime.now().day <= 8:
            for i, rule in enumerate(self.additional_rules):
                if rule.name == 'Alya BD':
                    result.append(ShortRule(i, rule.name))
        return result


regulator = Regulator()

if __name__ == '__main__':
    print(regulator.get_rules())
