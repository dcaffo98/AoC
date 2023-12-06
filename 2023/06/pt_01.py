
import python_utils as utils
from collections import defaultdict, namedtuple
from math import prod

race = namedtuple('race', ['time', 'distance'])


DEBUG_INPUT = """Time:      7  15   30
Distance:  9  40  200"""

INPUT_FILENAME = 'data/2023/06/input.txt'


def find_solutions(race):
    out = []
    time, distance = race
    for t in range(1, time):
        race_time = time - t
        if race_time * t > distance:
            out.append(t)
    return out

if __name__ == '__main__':
    if utils.is_debug():
        data = DEBUG_INPUT
    else:
        with open(INPUT_FILENAME, 'r') as f:
            data = f.read()

    time, distances = data.splitlines()

    times = time.split(':')[1].strip()
    distances = distances.split(':')[1].strip()

    times = list(map(int, times.split()))
    distances = list(map(int, distances.split()))
    races = [(t, d) for t, d in zip(times, distances)]

    solutions = []
    for race in races:
        solutions.append(find_solutions(race))
    
    sol_len = [len(x) for x in solutions]
    print(prod(sol_len))
    