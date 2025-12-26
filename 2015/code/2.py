import os

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def part1(puzzle: str):
    total = 0
    # surface area
    for line in puzzle.splitlines():
        l, w, h = map(int, line.split("x"))
        total += 2 * l * w + 2 * w * h + 2 * l * h + min(l * w, w * h, l * h)
    return total


def part2(puzzle: str):
    total = 0
    for line in puzzle.splitlines():
        s1, s2, s3 = sorted(map(int, line.split("x")))
        total += 2 * (s1 + s2) + s1 * s2 * s3
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
