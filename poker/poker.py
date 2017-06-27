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
    """Return a value indicating the ranking of a hand."""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, hand)


def card_ranks(cards):
    """Return a list of the ranks, sorted with higher first."""
    ranks = ['--23456789TJQKA'.index(rank) for rank, suit in cards]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def straight(ranks):
    """Return True if the ordered ranks form a 5-card straight."""
    # return sorted(range(min(ranks), max(ranks) + 1), reverse=True) == ranks
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand):
    """Return True if all the cards have the same suit."""
    suits = [suit for _, suit in hand]
    return len(set(suits)) == 1
    return kind(r, ranks)


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for rank in ranks:
        if ranks.count(rank) == n:
            return rank
    return None


def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None
