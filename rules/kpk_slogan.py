from app.types.rules import Rules, Block, Set

KPK_SLOGAN = Rules(
    'КПК с лозунгом',
    [Block('rules', [0]), Block('base', [0]), Block('rules', [1])],
    ['base', 'rules'],
    {
        'base': Set(['\n']),
        'rules': Set(['3', '4'], tags='r')
    }
)
