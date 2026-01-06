import os
import re

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def contains_abba(string):
    for a1, b1, b2, a2 in zip(string, string[1:], string[2:], string[3:]):
        if a1 == a2 and b1 == b2 and a1 != b1:
            return True
    return False


def get_babs(supernet_seqs):
    babs = set()
    for string in supernet_seqs:
        for a1, b, a2 in zip(string, string[1:], string[2:]):
            if a1 != b and a1 == a2:
                babs.add(f"{b}{a1}{b}")
    return babs


def part1(puzzle: str):
    total = 0

    for ip_address in puzzle.splitlines():
        parts = re.split(r"[\[\]]", ip_address)
        out_brackets = parts[0::2]
        in_brackets = parts[1::2]

        for string in out_brackets:
            if contains_abba(string):
                break
        else:
            continue

        for string in in_brackets:
            if contains_abba(string):
                break
        else:
            total += 1

    return total


def part2(puzzle: str):
    total = 0

    for ip_address in puzzle.splitlines():
        parts = re.split(r"[\[\]]", ip_address)
        out_brackets = parts[0::2]
        in_brackets = parts[1::2]

        babs = get_babs(out_brackets)

        for string in in_brackets:
            for b1, a, b2 in zip(string, string[1:], string[2:]):
                if b1 != b2 or f"{b1}{a}{b2}" not in babs:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        total += 1

    return total


def main():
    with open(f"../data/{day}/sample.txt", "r") as f:
        sample = f.read().strip()
    with open(f"../data/{day}/sample2.txt", "r") as f:
        sample2 = f.read().strip()
    with open(f"../data/{day}/input.txt", "r") as f:
        input = f.read().strip()

    print(f"{'='*60}")
    print("Part 1")
    if SAMPLE:
        print(f"Sample input: {part1(sample)}")
    if PUZZLE:
        print(f"Puzzle input: {part1(input)}")

    print(f"{'='*60}")
    print("Part 2")
    if SAMPLE:
        print(f"Sample input: {part2(sample2)}")
    if PUZZLE:
        print(f"Puzzle input: {part2(input)}")


if __name__ == "__main__":
    main()
