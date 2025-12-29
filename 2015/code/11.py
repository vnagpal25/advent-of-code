import os

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def increment(string):
    if string[-1] != "z":
        # increment
        return string[:-1] + chr(ord(string[-1]) + 1)
    else:
        # carry over
        return increment(string[:-1]) + "a"


def part1(puzzle: str):

    def is_valid(string):
        # condition 1: increasing sequence of characters
        condition = True
        condition &= any(
            ord(c) - ord(b) == 1 and ord(b) - ord(a) == 1
            for a, b, c in zip(string, string[1:], string[2:])
        )
        if not condition:
            return False
        # condition 2: can't contain i, o, or l
        condition &= "i" not in string and "o" not in string and "l" not in string
        # condition 3: two non overlapping distinct pairs
        if not condition:
            return False

        condition &= (
            sum(chr(num) + chr(num) in string for num in range(ord("a"), ord("z") + 1))
            >= 2
        )
        return condition

    while not is_valid(puzzle):
        puzzle = increment(puzzle)

    return puzzle


def part2(puzzle: str):
    first_pass = part1(puzzle)
    return part1(increment(first_pass))


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
