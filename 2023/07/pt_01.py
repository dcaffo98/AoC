
import python_utils as utils
from math import prod
from collections import OrderedDict, defaultdict
from functools import cmp_to_key

DEBUG_INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

INPUT_FILENAME = 'data/2023/07/input.txt'

CARDS = ('A K Q J T 9 8 7 6 5 4 3 2'.split()[::-1])
CARD_VALUES = OrderedDict({k: v for v, k in enumerate(CARDS)})


def score_hand(hand_str):
    counter = defaultdict(lambda: 0)
    for c in set(hand_str):
        counter[c] += hand_str.count(c)
    counts = list(counter.values())
    max_val = max(counts)
    if max_val == 5:
        return 7
    elif max_val == 4:
        return 6
    else:
        pair_count = counts.count(2)
        if max_val == 3:
            if pair_count == 1:
                return 5
            else:
                return 4
        elif max_val == 2:
            if pair_count == 2:
                return 3
            else:
                return 2
        else:
            # return - len(CARD_VALUES) + max([CARD_VALUES[c] for c in hand_str])
            return 1
        
        
def solve_tie(hand1, hand2):
    for i in range(len(hand1)):
        if CARD_VALUES[hand1[i]] > CARD_VALUES[hand2[i]]:
            return 1
        if CARD_VALUES[hand2[i]] > CARD_VALUES[hand1[i]]:
            return -1


def cmp(hand1, hand2):
    score1, score2 = score_hand(hand1[0]), score_hand(hand2[0])
    if score1 > score2:
        return 1
    elif score2 > score1:
        return -1
    else:
        return solve_tie(hand1[0], hand2[0])


if __name__ == '__main__':
    if utils.is_debug():
        data = DEBUG_INPUT
    else:
        with open(INPUT_FILENAME, 'r') as f:
            data = f.read()
    ALL_HANDS = [line.split() for line in data.splitlines()]
    
    hand_values = sorted(
        [(hand[0], hand[1]) for hand in ALL_HANDS],
        key=cmp_to_key(cmp),
        reverse=False
    )
    
    retval = sum(rank * int(hand_value[1]) for rank, hand_value in enumerate(hand_values, 1))
    print(retval)