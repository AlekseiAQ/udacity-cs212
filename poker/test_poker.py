import pytest

from poker import hand_rank, poker

straight_flush = "6c 7c 8c 9c Tc".split()
four_kind = "9d 9h 9s 9c 7d".split()
full_house = "Td Tc Th 7c 7d".split()
two_pair_1 = "5s 5d 9h 9c 6s".split()
straight_acelow = "AC 2D 4H 3D 5S".split()


HAND_RANK = (
    ('arg', 'expected'),
    [
        (straight_flush, (8, (10, 9, 8, 7, 6))),
        (four_kind, (7, (9, 7))),
        (full_house, (6, (10, 7))),
    ]
)


@pytest.mark.parametrize(*HAND_RANK)
def test_hand_rank(arg, expected):
    assert hand_rank(arg) == expected


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
