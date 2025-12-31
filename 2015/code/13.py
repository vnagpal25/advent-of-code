import os
from itertools import permutations
import re

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def part1(puzzle: str):
    names = set()
    happy_distances = {}
    pattern = r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)."

    for line in puzzle.splitlines():
        ((name1, sign, value, name2),) = re.findall(pattern, line)
        value = int(value)
        if sign == "lose":
            value *= -1

        names |= {name1, name2}

        happy_distances[(name1, name2)] = value

    max_happiness = float("-inf")

    for arrangement in permutations(names):
        happiness = 0
        for name1, name2 in zip(arrangement, arrangement[1:] + arrangement[:1]):
            happiness += (
                happy_distances[(name1, name2)] + happy_distances[(name2, name1)]
            )

        max_happiness = max(max_happiness, happiness)
    return max_happiness


def part2(puzzle: str):
    names = {"Vansh"}
    happy_distances = {}
    pattern = r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)."

    for line in puzzle.splitlines():
        ((name1, sign, value, name2),) = re.findall(pattern, line)
        value = int(value)
        if sign == "lose":
            value *= -1

        names |= {name1, name2}

        happy_distances[(name1, name2)] = value
        happy_distances[(name1, "Vansh")] = happy_distances[(name2, "Vansh")] = (
            happy_distances[("Vansh", name1)]
        ) = happy_distances[("Vansh", name2)] = 0

    max_happiness = float("-inf")

    for arrangement in permutations(names):
        happiness = 0
        for name1, name2 in zip(arrangement, arrangement[1:] + arrangement[:1]):
            happiness += (
                happy_distances[(name1, name2)] + happy_distances[(name2, name1)]
            )

        max_happiness = max(max_happiness, happiness)
    return max_happiness


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
