import sys
import os
sys.path.append(os.path.dirname(__file__))
from pt_01 import DEBUG_INPUT, INPUT_FILENAME, is_part
from collections import OrderedDict
import re
import python_utils as utils

if __name__ == '__main__':
    if utils.is_debug():
        data = DEBUG_INPUT
    else:
        with open(INPUT_FILENAME, 'r') as f:
            data = f.read()
    
    data = data.splitlines()
    parts = OrderedDict()
    gears = OrderedDict()
    for row, line in enumerate(data):
        part_row = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', line)]
        if any(part_row):
            parts[row] = part_row
        gear_row = [(m.start(0), m.end(0)) for m in re.finditer(r'\*', line)]
        if any(gear_row):
            gears[row] = gear_row

    gear_ratios = []
    for gear_row, candidate_gears in gears.items():
        for candidate_gear in candidate_gears:
            gear_idx = candidate_gear[0]
            matches = []
            for row in range(gear_row - 1, gear_row + 2):
                if row in parts:
                    for part in parts[row]:
                        if any([gear_idx == c for c in range(part[0] - 1, part[1] + 1)]):
                            matches.append(int(data[row][part[0]:part[1]]))
            if len(matches) == 2:
                gear_ratios.append(matches[0] * matches[1])
    print(sum(gear_ratios))

    # Correct answer: 87605697