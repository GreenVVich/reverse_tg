from app.types.rules import Rules, Block, Set

RUMORS = Rules(
    'Сплетени Финастры',
    [Block('characters'), Block('base', [0]), Block('acts'), Block('base', [0]),
     Block('characters'), Block('base', [0]), Block('acts2', [2, 3]), Block('base', [0]),
     Block('characters2'), Block('base', [0])],
    ['base', 'characters', 'acts'],
    {
        'base': Set([' ']),
        'characters': Set(['Маша', 'Дима', 'Тима', 'Валя', 'Юля', 'Маша', 'Кристина', 'Соня'], tags='u'),
        'characters2': Set(['Маше', 'Диме', 'Тиме', 'Вале', 'Юле', 'Маше', 'Кристине', 'Соне']),
        'acts': Set(['считает, что', 'уверяет всех, что', 'в тайне считает, что', 'отрицает, что']),
        'acts2': Set(['завидует', 'желает повышения', 'не нравится', 'распускает сплетни о', 'мешает работать'])
    }
)
