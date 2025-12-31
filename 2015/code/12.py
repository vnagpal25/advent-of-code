import os
import re
import json

day = os.path.basename(__file__).split(".")[0]

SAMPLE = False
PUZZLE = True


def part1(puzzle: str):
    return sum(map(int, re.findall(r"(-?\d+)", puzzle)))


def part2(puzzle: str):
    puzzle = json.loads(puzzle)

    def n(object):
        # if the object is an int, we return it
        if type(object) == int:
            return object
        if type(object) == list:
            return sum([n(j) for j in object])
        if type(object) != dict:
            return 0
        if "red" in object.values():
            return 0
        
        return n(list(object.values()))

    print(n(puzzle))


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
