from app.types.rules import Rules, Block, Set

TEST = Rules(
    'Тест',
    [Block('rules', [0]), Block('base', [0]), Block('rules', [1]), Block('base', [0]),
     Block('rules', [2]), Block('base', [0]), Block('rules', [3]), Block('base', [0]),
     Block('rules', [4]), Block('base', [0]), Block('rules')],
    ['base', 'rules'],
    {
        'base': Set(['\n--\n']),
        'rules': Set(['0', '1', '2', '3', '4'], tags='r')
    }
)

