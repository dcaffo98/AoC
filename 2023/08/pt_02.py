import os
import sys
sys.path.append(os.path.dirname(__file__))
from pt_01 import step, INPUT_FILENAME
import python_utils as utils
from itertools import cycle
import math

DEBUG_INPUT = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

if __name__ == '__main__':
    if utils.is_debug():
        data = DEBUG_INPUT
    else:
        with open(INPUT_FILENAME, 'r') as f:
            data = f.read()

    data = data.splitlines()
    INSTUCTIONS = data[0]
    MAP = [list(map(lambda x: x.strip(), line.split('='))) for line in data[2:]]
    MAP = {line[0]: line[1].replace(',', '').replace('(', '').replace(')', '').split(' ') for line in MAP}

    dst_locations = [k for k in MAP if k.endswith('A')]
    step_counter = []
    for i, inst in enumerate(cycle(INSTUCTIONS)):
        dst_locations = [step(dst_loc, MAP, inst) for dst_loc in dst_locations]
        for dst_loc in dst_locations:
            if dst_loc.endswith('Z'):
                step_counter.append(i + 1)
        dst_locations = [dst_loc for dst_loc in dst_locations if not dst_loc.endswith('Z')]
        if not any(dst_locations):
            break
    print(math.lcm(*step_counter))


