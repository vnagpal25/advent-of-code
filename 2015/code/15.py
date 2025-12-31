import os
import re
import numpy as np

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def generate_groups_of_2():
    groups = set()
    for a in range(0, 101):
        b = 100 - a
        groups.add((a, b))

    return groups


def generate_groups_of_4():
    groups = set()
    for a in range(0, 101):
        for b in range(0, 101 - a):
            for c in range(0, 101 - a - b):
                d = 100 - a - b - c
                groups.add((a, b, c, d))
    return groups


def part1(puzzle: str):
    pattern = r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"

    properties = []
    for line in puzzle.splitlines():

        ing, *props = re.findall(pattern, line)[0]
        properties.append(list(map(int, props[:-1])))

    if len(properties) == 2:
        combinations = generate_groups_of_2()
    else:
        combinations = generate_groups_of_4()

    properties = np.array(properties)

    max_score = float("-inf")
    for amounts in combinations:
        amounts = np.array(amounts)
        props = amounts @ properties
        props = [prop if prop > 0 else 0 for prop in props]
        max_score = max(np.prod(props), max_score)

    return max_score


def part2(puzzle: str):
    pattern = r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"

    properties = []
    for line in puzzle.splitlines():

        ing, *props = re.findall(pattern, line)[0]
        properties.append(list(map(int, props)))

    if len(properties) == 2:
        combinations = generate_groups_of_2()
    else:
        combinations = generate_groups_of_4()

    properties = np.array(properties)

    max_score = float("-inf")
    for amounts in combinations:
        amounts = np.array(amounts)
        *props, cals = amounts @ properties

        if cals != 500:
            continue

        props = [prop if prop > 0 else 0 for prop in props]
        max_score = max(np.prod(props), max_score)

    return max_score


def main():
    with open(f"../data/{day}/sample.txt", "r") as f:
        sample = f.read().strip()
    with open(f"../data/{day}/input.txt", "r") as f:
        input = f.read().strip()

    print(f"{'='*60}")
    print("Part 1")
    if SAMPLE:
        print(part1(sample))
    if PUZZLE:
        print(part1(input))

    print(f"{'='*60}")
    print("Part 2")
    if SAMPLE:
        print(part2(sample))
    if PUZZLE:
        print(part2(input))


if __name__ == "__main__":
    main()
