import os
import re

day = os.path.basename(__file__).split(".")[0]

PUZZLE = True


def part1(puzzle: str):
    detected = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    pattern = r"Sue \d+: (.*?)$"
    candidates = []
    for i, line in enumerate(puzzle.splitlines()):
        props = re.findall(pattern, line)[0].split(", ")
        props = {string.split(": ")[0]: int(string.split(": ")[1]) for string in props}
        for prop, amt in props.items():

            if detected[prop] != amt:
                break
        else:
            candidates.append(i + 1)

    return candidates


def part2(puzzle: str):
    detected = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }
    pattern = r"Sue \d+: (.*?)$"
    candidates = []
    for i, line in enumerate(puzzle.splitlines()):
        props = re.findall(pattern, line)[0].split(", ")
        props = {string.split(": ")[0]: int(string.split(": ")[1]) for string in props}
        for prop, amt in props.items():
            if prop in ["cats", "trees"]:
                if amt <= detected[prop]:
                    break
            elif prop in ["pomeranians", "goldfish"]:
                if amt >= detected[prop]:
                    break
            elif detected[prop] != amt:
                break
        else:
            candidates.append(i + 1)

    return candidates


def main():
    with open(f"../data/{day}/input.txt", "r") as f:
        input = f.read().strip()

    print(f"{'='*60}")
    print("Part 1")

    if PUZZLE:
        print(part1(input))

    print(f"{'='*60}")
    print("Part 2")

    if PUZZLE:
        print(part2(input))


if __name__ == "__main__":
    main()
