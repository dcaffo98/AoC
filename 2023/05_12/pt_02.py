import os
import sys
sys.path.append(os.path.dirname(__file__))
from pt_01 import *
import python_utils as utils
from collections import OrderedDict
import multiprocessing as mlp
from functools import partial
from random import random
import numpy as np
from ctypes import c_ulong


# mlp.set_start_method('fork')

def np_step(sources, src2dst):
    destinations = sources.copy()
    for line in src2dst:
        dst_start, src_start, length = line
        mask = (sources >= src_start) & (sources < src_start + length)
        destinations[mask] = dst_start + sources[mask] - src_start
    return destinations

def func(i, **kwargs):
    maps = kwargs['maps']
    ranges = kwargs['ranges']
    min_location = kwargs['min_location']
    count = kwargs['count']

    sources = np.fromiter(ranges[i], np.uint32)
    for _, mapping in maps.items():
        sources = np_step(sources, mapping)
    local_min = sources.min().item()
    if local_min < min_location.value:
        min_location.value = local_min
    count.value += len(sources)
    if random() > 0.9999:
        print(f"{(count.value / kwargs['n_seeds'] * 100):.2f}%")


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
    SEED_RANGES = MAPS.pop('seeds')[0]

    # L = 2014246223
    N_PROC = 6
    chunksize = 5000
    L = sum(SEED_RANGES[1::2])
    print(f"Total seeds: {L}")

    manager = mlp.Manager()
    ranges = manager.list([
        range(i, min(i + chunksize, seed_start + seed_len)) \
        for seed_start, seed_len in zip(SEED_RANGES[::2], SEED_RANGES[1::2]) \
        for i in range(seed_start, seed_start + seed_len, chunksize)
    ])
    min_location = manager.Value(c_ulong, 2 ** 32 -1)
    count = manager.Value(c_ulong, 0)

    _func = partial(
        func,
        maps=MAPS,
        ranges=ranges,
        n_seeds=L,
        min_location=min_location,
        count=count
    )

    with mlp.Pool(N_PROC) as p:
        print("Starting...")
        p.map(_func, list(range(len(ranges))))

    print(f"Min location: {min_location.value}")

    # Correct answer: 100165128
    # Took ~10 minutes on my MacBook Air M2