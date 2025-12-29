import os
import re

from itertools import permutations

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def part1(puzzle: str):
    pattern = "(\w+) to (\w+) = (\d+)"
    cities = set()
    distances = {}
    for line in puzzle.splitlines():
        a, b, dist = re.match(pattern, line).groups()
        dist = int(dist)
        cities |= {a, b}
        distances[(a, b)] = dist
        distances[(b, a)] = dist

    min_length = float("inf")
    for perm in permutations(cities):
        length = 0
        for a, b in zip(perm, perm[1:]):
            length += distances[(a, b)]
        min_length = min(min_length, length)
    return min_length


def part2(puzzle: str):
    pattern = "(\w+) to (\w+) = (\d+)"
    cities = set()
    distances = {}
    for line in puzzle.splitlines():
        a, b, dist = re.match(pattern, line).groups()
        dist = int(dist)
        cities |= {a, b}
        distances[(a, b)] = dist
        distances[(b, a)] = dist

    max_length = float("-inf")
    for perm in permutations(cities):
        length = 0
        for a, b in zip(perm, perm[1:]):
            length += distances[(a, b)]
        max_length = max(max_length, length)
    return max_length


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
