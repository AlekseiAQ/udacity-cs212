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


count_rankings = {
    (5,): 10,  # 5 of a kind
    (4, 1): 7,  # 4 of a kind
    (3, 2): 6,  # full house
    (3, 1, 1): 3,  # 3 of a kind
    (2, 2, 1): 2,  # 2 pair
    (2, 1, 1, 1): 1,  # 1 pair
    (1, 1, 1, 1, 1): 0,  # high card
}


def hand_rank(hand):
    """Return a velue indicating how high the hand ranks."""
    groups = group(['--23456789TJQKA'.index(rank) for rank, _ in hand])
    counts, ranks = zip(*groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([suit for _, suit in hand])) == 1
    return max(count_rankings.get(counts), 4 * straight + 5 * flush), ranks


def group(items):
    """Return a list of [(count, x)...], highest count first,
    then highest x first."""
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)
