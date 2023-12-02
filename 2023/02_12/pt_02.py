import sys
sys.path.append('2023/02_12')
from pt_01 import DEBUG_INPUT, INPUT_FILENAME
from collections import defaultdict
import numpy as np
from math import prod

is_debug = 'pydevd' in sys.modules


def min_cubes(line: str):
    _, data_str = line.split(':')

    min_cubes = defaultdict(lambda: 0)
    for hand in data_str.split(';'):
        for hand_cube in hand.split(','):
            n, color = hand_cube.strip().split(' ')
            min_cubes[color] = max(min_cubes[color], int(n))
    return min_cubes

def cube_set_power(cubes: dict):
    return np.prod(np.array(list(cubes.values())))


if __name__ == '__main__':
    if is_debug:
        data = DEBUG_INPUT.splitlines()
    else:
        with open(INPUT_FILENAME, 'r') as f:
            data = f.readlines()

    min_cubes = [min_cubes(line) for line in data]
    result = sum(cube_set_power(x) for x in min_cubes)
    print(result)

    # Correct answer: 63700