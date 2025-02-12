from app.types.rules import Rules, Block, Set

REV_EXO_RULE = Rules(
    'Обратный экзорцизм',
    [Block('characters'), Block('base', [0]), Block('acts', [0, 1]), Block('base', [0]),
     Block('characters'), Block('base', [2]), Block('acts', [2, 3]), Block('base', [0]),
     Block('characters'), Block('base', [1])],
    ['base', 'characters', 'acts'],
    {
        'base': Set([' ', 'а', 'а ']),
        'characters': Set(['священник', 'дьявол', 'мальчик']),
        'acts': Set(['просит', 'требует', 'выйти из', 'войти в'])
    }
)
