import sys
from collections import OrderedDict
import re
import python_utils as utils

DEBUG_INPUT = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

INPUT_FILENAME = 'data/2023/03_12/engine_parts.txt'


def is_part(lines, row, start, end):
    L = len(next(iter(lines)))
    N_lines = len(lines)
    top_row = max(0, row - 1)
    bottom_row = min(N_lines, row + 2)
    left = max(start - 1, 0)
    right = min(end + 1, L)

    for _ in range(start, end):
        for r in range(top_row, bottom_row):
            for c in range(left, right):
                char = lines[r][c]
                if not char.isdigit() and char != '.':
                    return int(lines[row][start:end])
    else:
        return 0

if __name__ == '__main__':
    if utils.is_debug():
        data = DEBUG_INPUT
    else:
        with open(INPUT_FILENAME, 'r') as f:
            data = f.read()
    
    data = data.splitlines()
    numbers = OrderedDict()
    for row, line in enumerate(data):
        numbers[row] = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', line)]
    
    parts = [is_part(data, row, match[0], match[1]) for row, matches in numbers.items() for match in matches if any(next(iter(matches)))]
    print(sum(parts)) 

    # Correct answer: 540212