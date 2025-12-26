import os
from collections import Counter, defaultdict

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def part1(puzzle: str):
    # must contain at least three vowels
    # one letter must appear twice in a row
    # can't contain ab, cd, pq, or xy
    total = 0
    for string in puzzle.splitlines():
        letter_counts = Counter(string)

        # check vowel counts
        if (
            letter_counts.get("a", 0)
            + letter_counts.get("e", 0)
            + letter_counts.get("i", 0)
            + letter_counts.get("o", 0)
            + letter_counts.get("u", 0)
            < 3
        ):
            continue

        twice_row = False
        forbidden = {"ab": False, "cd": False, "pq": False, "xy": False}
        for a, b in zip(string, string[1:]):
            if a == b:
                twice_row = True

            if a + b in forbidden.keys():
                forbidden[a + b] = True
        if not twice_row or any(forbidden.values()):
            continue

        total += 1
    return total


def part2(puzzle: str):

    total = 0
    for string in puzzle.splitlines():
        pair_index_map = defaultdict(list)
        for i, (a, b) in enumerate(zip(string, string[1:])):
            pair_index_map[a + b].append(i)

        pair_condition = False
        for indices in pair_index_map.values():
            if len(indices) == 1:
                continue

            diffs = [j - i for i, j in zip(indices, indices[1:])]
            for diff in diffs:
                if diff >= 2:
                    pair_condition = True

        if not pair_condition:
            continue

        for a, b in zip(string, string[2:]):
            if a == b:
                total += 1
                break

    return total


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
