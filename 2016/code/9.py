import os
import re

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def part1(compressed: str):
    decompressed = ""
    pattern = r"\(\d+x\d+\)"
    while compressed:
        match = re.search(pattern, compressed)
        if not match:
            decompressed += compressed
            break
        l, r = match.span()

        # parse marker
        length, reps = map(int, match.group(0)[1:-1].split("x"))

        # append everything to the left of the marker
        decompressed += compressed[:l]

        # append repititions of following segment
        decompressed += compressed[r : r + length] * reps

        compressed = compressed[r + length :]

    return len(decompressed)


def part2(compressed: str):
    # will use a recursive stack-based approach to decode
    # won't store raw decompressed string, will only store the total number of characters
    def count_length(s):
        total = 0
        i = 0
        while i < len(s):
            if s[i] == "(":
                j = s.find(")", i)
                length, reps = map(int, s[i + 1 : j].split("x"))
                total += reps * count_length(s[j + 1 : j + 1 + length])
                i = j + 1 + length
            else:
                total += 1
                i += 1
        return total

    return count_length(compressed)


def main():
    with open(f"../data/{day}/sample.txt", "r") as f:
        sample = f.read().strip()
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
        print(f"Sample input: {part2(sample)}")
    if PUZZLE:
        print(f"Puzzle input: {part2(input)}")


if __name__ == "__main__":
    main()
