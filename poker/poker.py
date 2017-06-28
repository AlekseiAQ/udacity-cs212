import random

deck_52 = [rank + suit for rank in '23456789TJQKA' for suit in 'shdc']


def deal(numhands, n=5, deck=deck_52):
    """Shuffle the deck and deal out numhands n-card hands."""
    random.shuffle(deck)
    return [deck[0 + n * i:n * (i + 1)] for i in range(numhands)]


def poker(hands):
    """Return a list of winning hands: poker([hand,...]) => [hand,...]"""
    winner_hands = allmax(hands, key=hand_rank)
    return winner_hands if len(winner_hands) > 1 else winner_hands[0]


def allmax(iterable, key=None):
    """Return a list of all items equal to the max of the iterable."""
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        if not result or xval > maxval:
            result, maxval = [x], xval
        elif xval == maxval:
            result.append(x)
    return result


def hand_rank(hand):
    """Return a velue indicating how high the hand ranks."""
    groups = group(['--23456789TJQKA'.index(rank) for rank, _ in hand])
    counts, ranks = zip(*groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([suit for _, suit in hand])) == 1
    return (9 if (5,) == counts else  # 5 of a kind
            8 if straight and flush else  # straight flush
            7 if (4, 1) == counts else  # 4 of a kind
            6 if (3, 2) == counts else  # full house
            5 if flush else  # flush
            4 if straight else  # straight
            3 if (3, 1, 1) == counts else  # 3 of a kind
            2 if (2, 2, 1) == counts else  # 2 pair
            1 if (2, 1, 1, 1) == counts else  # kind
            0), ranks  # high card


def group(items):
    """Return a list of [(count, x)...], highest count first, then highest x first."""
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)
