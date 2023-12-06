import sys
import os
sys.path.append(os.path.dirname(__file__))
from pt_01 import DEBUG_INPUT, INPUT_FILENAME, find_solutions
import python_utils as utils
from math import prod

if __name__ == '__main__':
    if utils.is_debug():
        data = DEBUG_INPUT
    else:
        with open(INPUT_FILENAME, 'r') as f:
            data = f.read()

    time, distances = data.splitlines()

    times = time.split(':')[1].strip()
    distances = distances.split(':')[1].strip()

    times = [int(times.replace(' ', ''))]
    distances = [int(distances.replace(' ', ''))]
    races = [(t, d) for t, d in zip(times, distances)]

    solutions = []
    for race in races:
        solutions.append(find_solutions(race))
    
    # print(solutions)
    sol_len = [len(x) for x in solutions]
    print(prod(sol_len))
    