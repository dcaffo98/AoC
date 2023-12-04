import sys
import os
sys.path.append(os.path.dirname(__file__))
from pt_01 import DEBUG_INPUT, INPUT_FILENAME
import python_utils as utils
from collections import defaultdict


if __name__ == '__main__':
    if utils.is_debug():
        data = DEBUG_INPUT
    else:
        with open(INPUT_FILENAME, 'r') as f:
            data = f.read()

    data = data.splitlines()
    data = [l.split(':')[1] for l in data]

    datalines = [list(map(int, (y for y in x.strip().split(' ') if y))) for line in data for x in line.split('|')]
    datalines = [datalines[i:i+2] for i in range(0, len(datalines), 2)]

    matches = defaultdict(list)
    [matches[line_idx].append((idx, n)) for line_idx, line in enumerate(datalines) for idx, n in enumerate(line[1]) if n in line[0]]
    
    copy_counters = defaultdict(lambda: 0)
    for card_id, values in matches.items():
        copy_counters[card_id] += 1
        for i in range(card_id + 1, card_id + len(values) + 1):
            copy_counters[i] += copy_counters[card_id]

    tot = sum(copy_counters.values())
    if len(matches) < len(datalines):
        tot += (len(datalines) - len(matches))
    print(tot)  

    # Correct answer: 6050769