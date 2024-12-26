from managers.rule import Actor, Action, Rules


class Regulator:
    actors: list[Actor] = [Actor(['священник', 'священника', 'священнику',
                                  'священника', 'священником', 'священнике']),
                           Actor(['дьявол', 'дьявола', 'дьяволу',
                                 'дьявола', 'дьяволом', 'дьяволе']),
                           Actor(['мальчик', 'мальчика', 'мальчику',
                                 'мальчика', 'мальчиком', 'мальчике'])]
    first_action: list[Action] = [Action('просит', 1), Action('запрещает', 2)]
    second_action: list[Action] = [Action('выйти из', 3), Action('войти в', 3)]

    def get_rules(self) -> Rules:
        return Rules(self.actors,  self.first_action, self.second_action)

    def update_rules(self) -> None:
        ...  # TODO


regulator = Regulator()

if __name__ == '__main__':

    print(regulator.get_rules())
