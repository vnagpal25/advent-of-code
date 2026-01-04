import os
from itertools import permutations

day = os.path.basename(__file__).split(".")[0]

PUZZLE = True


def part1(puzzle: str):
    count = 0
    for line in puzzle.splitlines():
        sides = list(map(int, line.split()))
        for s1, s2, s3 in permutations(sides):
            if s1 + s2 <= s3:
                break
        else:
            count += 1
    return count


def part2(puzzle: str):
    count = 0
    # stack columns together
    puzzle = sum(map(list, list(zip(*map(str.split, puzzle.splitlines())))), [])

    for i in range(0, len(puzzle), 3):
        sides = map(int, puzzle[i : i + 3])
        for s1, s2, s3 in permutations(sides):
            if s1 + s2 <= s3:
                break
        else:
            count += 1
    return count


def main():
    with open(f"../data/{day}/sample.txt", "r") as f:
        sample = f.read().strip()
    with open(f"../data/{day}/input.txt", "r") as f:
        input = f.read().strip()

    print(f"{'='*60}")
    print("Part 1")
    if PUZZLE:
        print(f"Puzzle input: {part1(input)}")

    print(f"{'='*60}")
    print("Part 2")
    if PUZZLE:
        print(f"Puzzle input: {part2(input)}")


if __name__ == "__main__":
    main()
