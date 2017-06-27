import pytest

from poker import card_ranks, flush, hand_rank, kind, poker, straight, two_pair

straight_flush = "6c 7c 8c 9c Tc".split()
four_kind = "9d 9h 9s 9c 7d".split()
full_house = "Td Tc Th 7c 7d".split()
two_pair_1 = "5s 5d 9h 9c 6s".split()
straight_acelow = "AC 2D 4H 3D 5S".split()

four_kind_ranks = card_ranks(four_kind)
two_pair_ranks = card_ranks(two_pair_1)

CARD_RANKS = (
    ('arg', 'expected'),
    [
        (straight_flush, [10, 9, 8, 7, 6]),
        (four_kind, [9, 9, 9, 9, 7]),
        (full_house, [10, 10, 10, 7, 7]),
    ]
)


@pytest.mark.parametrize(*CARD_RANKS)
def test_card_ranks(arg, expected):
    assert card_ranks(arg) == expected


HAND_RANK = (
    ('arg', 'expected'),
    [
        (straight_flush, (8, 10)),
        (four_kind, (7, 9, 7)),
        (full_house, (6, 10, 7)),
    ]
)


@pytest.mark.parametrize(*HAND_RANK)
def test_hand_rank(arg, expected):
    assert hand_rank(arg) == expected


KIND = (
    ('args', 'expected'),
    [
        ((4, four_kind_ranks), 9),
        ((3, four_kind_ranks), None),
        ((2, four_kind_ranks), None),
        ((1, four_kind_ranks), 7),
    ]
)


@pytest.mark.parametrize(*KIND)
def test_kind(args, expected):
    assert kind(*args) == expected


TWO_PAIR = (
    ('arg', 'expected'),
    [
        (four_kind_ranks, None),
        (two_pair_ranks, (9, 5)),
    ]
)


@pytest.mark.parametrize(*TWO_PAIR)
def test_two_pair(arg, expected):
    assert two_pair(arg) == expected


# assert two_pair(four_kind_ranks) == None
# assert two_pair(two_pair_ranks) == (9, 5)

STRAIGHT = (
    ('arg', 'expected'),
    [
        (card_ranks(straight_acelow), True),
        ([9, 8, 7, 6, 5], True),
        ([9, 8, 8, 6, 5], False),
    ]
)


@pytest.mark.parametrize(*STRAIGHT)
def test_straight(arg, expected):
    assert straight(arg) == expected


# assert straight(card_ranks(straight_acelow)) == True
# assert straight([9, 8, 7, 6, 5]) == True
# assert straight([9, 8, 8, 6, 5]) == False

FLUSH = (
    ('arg', 'expected'),
    [
        (straight_flush, True),
        (four_kind, False),
    ]
)


@pytest.mark.parametrize(*FLUSH)
def test_flush(arg, expected):
    assert flush(arg) == expected


POKER = (
    ('arg', 'expected'),
    [
        ([straight_flush, four_kind, full_house], straight_flush),
        ([four_kind, full_house], four_kind),
        ([full_house, full_house], [full_house, full_house]),
        ([four_kind], four_kind),
        ([straight_flush] + 99 * [full_house], straight_flush),
    ]
)


@pytest.mark.parametrize(*POKER)
def test_poker(arg, expected):
    assert poker(arg) == expected
