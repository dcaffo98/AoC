
import python_utils as utils
from collections import defaultdict


DEBUG_INPUT = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

INPUT_FILENAME = 'data/2023/04_12/input.txt'

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

    tot = 0
    for match, values in matches.items():
        tot += (2 ** (len(values) - 1))

    print(tot)