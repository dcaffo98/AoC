import python_utils as utils
from itertools import cycle
from collections import OrderedDict
import re
import numpy as np


DEBUG_INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
   
INPUT_FILENAME = 'data/2023/09/input.txt'


def process_line(line):
    line = np.array(line)
    diff = np.diff(line)
    differences = [line, diff]
    while not np.all(diff == 0):
        diff = np.diff(diff)
        differences.append(diff)
    to_sub = 0
    for diff in differences[::-1][1:]:
        to_sub = diff[0] - to_sub
    return to_sub
        

if __name__ == '__main__':
    if utils.is_debug():
        data = DEBUG_INPUT
    else:
        with open(INPUT_FILENAME, 'r') as f:
            data = f.read()

    report = [list(map(int, re.findall('-?\d+', line))) for line in data.splitlines()]
    new_values = [process_line(line) for line in report]
    print(sum(new_values))