import sys
import os
sys.path.append(os.path.dirname(__file__))
from pt_01 import DEBUG_INPUT, INPUT_FILENAME
import python_utils as utils
from math import prod
from functools import cmp_to_key
from collections import defaultdict, OrderedDict

CARDS = ('A K Q T 9 8 7 6 5 4 3 2 J'.split()[::-1])
CARD_VALUES = OrderedDict({k: v for v, k in enumerate(CARDS)})


def solve_tie(hand1, hand2):
    for i in range(len(hand1)):
        if CARD_VALUES[hand1[i]] > CARD_VALUES[hand2[i]]:
            return 1
        if CARD_VALUES[hand2[i]] > CARD_VALUES[hand1[i]]:
            return -1
        

def score_hand_joker_wise(hand_str):
    counter = defaultdict(lambda: 0)
    for c in set(hand_str):
        counter[c] += hand_str.count(c)
    n_jokers = counter.pop('J', 0)
    # if n_jokers:
        # breakpoint()
    counts = list(counter.values())
    max_val = max(counts) if any(counts) else 0
    joker_max_val = min(5, max_val + n_jokers)
    if max_val == 5:
        return 7
    elif max_val == 4:
        if joker_max_val == 5:
            return 7
        else:
            return 6
    else:
        pair_count = counts.count(2)
        if max_val == 3:
            if joker_max_val == 5:
                return 7
            elif joker_max_val == 4:
                return 6
            elif pair_count == 1 or n_jokers > 1:
                return 5
            else:
                return 4
        elif max_val == 2:
            if joker_max_val == 5:
                return 7
            elif joker_max_val == 4:
                return 6
            elif (pair_count == 2 and n_jokers) or (pair_count == 1 and n_jokers > 2):
                return 5
            elif joker_max_val == 3:
                return 4
            elif pair_count == 2 or (pair_count == 1 and n_jokers == 2):
                return 3
            else:
                if joker_max_val == 5:
                    return 7
                elif joker_max_val == 4:
                    return 6
                elif joker_max_val == 3:
                    return 5
                else:
                    return 2
        elif joker_max_val == 5:
            return 7
        elif joker_max_val == 4:
            return 6
        elif joker_max_val == 3:
            return 4
        elif joker_max_val == 2:
            return 2
    return 1


def cmp(hand1, hand2):
    score1, score2 = score_hand_joker_wise(hand1[0]), score_hand_joker_wise(hand2[0])
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