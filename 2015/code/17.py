import os
from itertools import combinations

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def part1(puzzle: str, n):
    containers = [int(container) for container in puzzle.splitlines()]

    total = 0
    for num_containers in range(1, len(containers) + 1):
        for combination in combinations(containers, num_containers):
            total += sum(combination) == n

    return total


def part2(puzzle: str, n):
    containers = [int(container) for container in puzzle.splitlines()]

    for num_containers in range(1, len(containers) + 1):
        total = 0
        for combination in combinations(containers, num_containers):
            total += sum(combination) == n

        if total:
            return total



def main():
    with open(f"../data/{day}/sample.txt", "r") as f:
        sample = f.read().strip()
    with open(f"../data/{day}/input.txt", "r") as f:
        input = f.read().strip()

    print(f"{'='*60}")
    print("Part 1")
    if SAMPLE:
        print(part1(sample, 25))
    if PUZZLE:
        print(part1(input, 150))

    print(f"{'='*60}")
    print("Part 2")
    if SAMPLE:
        print(part2(sample, 25))
    if PUZZLE:
        print(part2(input, 150))


if __name__ == "__main__":
    main()
