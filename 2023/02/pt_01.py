import sys

is_debug = 'pydevd' in sys.modules

DEBUG_INPUT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
INPUT_FILENAME = 'data/2023/02/game_list.txt'

MAX_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def is_valid(line: str):
    game_str, data_str = line.split(':')
    game_id = int(game_str.split(' ')[-1])

    valid = True
    for hand in data_str.split(';'):
        for hand_cube in hand.split(','):
            n, color = hand_cube.strip().split(' ')
            if int(n) > MAX_CUBES[color]:
                valid = False
                break
    
    return (game_id, valid)


if __name__ == '__main__':
    if is_debug:
        data = DEBUG_INPUT.splitlines()
    else:
        with open(INPUT_FILENAME, 'r') as f:
            data = f.readlines()

    ids = [is_valid(line) for line in data]
    valid_ids = [item[0] for item in ids if item[1]]
    print(f"valid games: {valid_ids}\n\nSum: {sum(valid_ids)}")