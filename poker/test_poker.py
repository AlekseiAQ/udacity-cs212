import pytest

from poker import hand_rank, poker

straight_flush = "6c 7c 8c 9c Tc".split()
four_kind = "9d 9h 9s 9c 7d".split()
full_house = "Td Tc Th 7c 7d".split()
flush = "Ad Kd Td 8d 7d".split()
straight = "Qd Jc Th 9c 8c".split()
straight_acelow = "Ac 2d 4h 3d 5s".split()
three_of_kind = "Ac Ad Ah 3d 5s".split()
two_pair = "5s 5d 9h 9c 6s".split()
one_pair = "5s 5d 8h 9c 6s".split()
ace_high = "As 2c 3h Kc Qc".split()


HAND_RANK = (
    ('arg', 'expected'),
    [
        (straight_flush, (9, (10, 9, 8, 7, 6))),
        (four_kind, (7, (9, 7))),
        (full_house, (6, (10, 7))),
        (flush, (5, (14, 13, 10, 8, 7))),
        (straight, (4, (12, 11, 10, 9, 8))),
        (straight_acelow, (4, (5, 4, 3, 2, 1))),
        (three_of_kind, (3, (14, 5, 3))),
        (two_pair, (2, (9, 5, 6))),
        (one_pair, (1, (5, 9, 8, 6))),
        (ace_high, (0, (14, 13, 12, 3, 2))),
    ]
)


@pytest.mark.parametrize(*HAND_RANK)
def test_hand_rank(arg, expected):
    assert hand_rank(arg) == expected


POKER = (
    ('arg', 'expected'),
    [
        ([ace_high, one_pair], one_pair),
        ([straight_acelow, straight], straight),
        ([flush, one_pair], flush),
        ([two_pair, flush, straight, full_house, two_pair], full_house),
        ([one_pair, flush, straight, one_pair, two_pair], flush),
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
