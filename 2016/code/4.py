import os
import re
from collections import Counter

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def part1(puzzle: str):
    total = 0
    for room in puzzle.splitlines():
        *name, id_checksum = room.split("-")
        name = "".join(name)
        ((id, checksum),) = re.findall(r"(\d+)\[(\w+)\]", id_checksum)
        letter_counts = Counter(name)
        # -x[1] sorts in descending value by frequency
        # x[0] breaks ties alphabetically
        sorted_items = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))

        # recalculated checksum
        recalculated = "".join([x[0] for x in sorted_items][: len(checksum)])

        if recalculated == checksum:
            total += int(id)
    return total


def part2(puzzle: str):

    def rotate(string, number):
        new = ""
        for ch in string:
            new += chr(ord("a") + (ord(ch) + number - ord("a")) % 26)
        return new

    for room in puzzle.splitlines():
        *name, id_checksum = room.split("-")
        ((id, _),) = re.findall(r"(\d+)\[(\w+)\]", id_checksum)

        id = int(id)

        rotated_name = " ".join([rotate(word, id) for word in name])
        if "north" in rotated_name:
            print(rotated_name, id)


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
