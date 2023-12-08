import python_utils as utils
from itertools import cycle
from collections import OrderedDict

DEBUG_INPUT = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""
# DEBUG_INPUT = """RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)"""
   
INPUT_FILENAME = 'data/2023/08/input.txt'


def step(start_location, MAP, instruction):
    if instruction == 'L':
        return MAP[start_location][0]
    elif instruction == 'R':
        return MAP[start_location][1]
    else:
        raise ValueError()

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
    
    dst_location = 'AAA'
    for i, inst in enumerate(cycle(INSTUCTIONS)):
        dst_location = step(dst_location, MAP, inst)    
        if dst_location == 'ZZZ':
            print(i + 1)
            break