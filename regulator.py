from typing import Dict


class Regulator:
    actors: list[str] = ['священник', 'дьявол', 'мальчик']
    first_action: list[str] = [' говорит ', ' запрещает ']
    second_action: list[str] = [' выйти из ', ' войти в ']

    def get_rules(self) -> Dict[str, list[str]]:
        return {'actors': self.actors, 'first_action': self.first_action, 'second_action': self.second_action}

    def update_rules(self) -> None:
        ...


regulator = Regulator()

if __name__ == '__main__':
    from random import choice
    print(choice(regulator.get_rules()['actors']))
