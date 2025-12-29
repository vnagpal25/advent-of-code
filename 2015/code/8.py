import os

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def part1(puzzle: str):
    total = 0
    for string in puzzle.splitlines():
        # strip surrounding quotes
        decoded = string[1:-1]
        while "\\" in decoded:
            slash_ind = decoded.find("\\")

            if decoded[slash_ind + 1] == "x":
                # hexadecimal case
                decoded = decoded[:slash_ind] + "~" + decoded[slash_ind + 4 :]
            else:
                # \\ or \" case
                decoded = decoded[:slash_ind] + "~" + decoded[slash_ind + 2 :]
        total += len(string) - len(decoded)
    return total


def part2(puzzle: str):
    total = 0
    for string in puzzle.splitlines():
        # escape all backslashes
        encoded = string.replace("\\", "\\\\")

        # escape all quotes
        encoded = encoded.replace('"', '\\"')

        # preceding and following quote
        encoded = f'"{encoded}"'
        total += len(encoded) - len(string)
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
