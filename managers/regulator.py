from managers.rules import Char, Act, Block, Rules


class Regulator:
    rules: list[Rules] = [Rules(
        [Block(1, [1, 2, 3]), Block(0, None, ' '), Block(2, [1, 2]), Block(0, None, ' '),
         Block(1, [1, 2, 3]), Block(0, None, ' '), Block(2, [3, 4]), Block(0, None, ' '),
         Block(1, [1, 2, 3])],
        [Char(['священник', 'священника', 'священнику',
               'священника', 'священником', 'священнике']),
         Char(['дьявол', 'дьявола', 'дьяволу',
               'дьявола', 'дьяволом', 'дьяволе']),
         Char(['мальчик', 'мальчика', 'мальчику',
               'мальчика', 'мальчиком', 'мальчике'])],
        [Act('просит', 1), Act('запрещает', 2), Act('выйти из', 3), Act('войти в', 3)]), ]

    def get_rules(self, selected_rule: int) -> Rules:
        return self.rules[selected_rule]

    def update_rules(self) -> None:
        ...  # TODO


regulator = Regulator()

if __name__ == '__main__':
    print(regulator.get_rules())
