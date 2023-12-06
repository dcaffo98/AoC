
from typing import List
import python_utils as utils
from collections import OrderedDict


DEBUG_INPUT = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

INPUT_FILENAME = 'data/2023/05/input.txt'

'''
the destination range start, the source range start, and the range length [,)
'''

def step(
    sources: List[int],
    src2dst: List[List[int]]
) -> List[int]:
    destinations = []
    for src in sources:
        dst = src
        for line in src2dst:
            dst_start, src_start, length = line
            if src >= src_start and src < src_start + length:
                dst = dst_start + src - src_start
        destinations.append(dst)
    return destinations


if __name__ == '__main__':
    if utils.is_debug():
        data = DEBUG_INPUT
    else:
        with open(INPUT_FILENAME, 'r') as f:
            data = f.read()

    MAPS = OrderedDict()
    for block in data.split('\n\n'):
        k, values = block.split(':')
        MAPS[k.strip()] = [list(map(int, x.split())) for x in values.strip().split('\n')]
    SEEDS = MAPS.pop('seeds')[0]

    inputs = SEEDS
    for key, mapping in MAPS.items():
        inputs = step(inputs, mapping)

    print(min(inputs))

    # Correct answer: 178159714
    