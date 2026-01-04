import os

day = os.path.basename(__file__).split(".")[0]

PUZZLE = False


def part1():
    # (2978, 3083)
    num = 20151125
    for diagonal in range(2, 6062):
        for c in range(1, diagonal):
            if (diagonal - c, c) == (2978, 3083):
                return num
            num *= 252533
            num %= 33554393


def main():
    print(f"{'='*60}")
    print("Part 1")
    print(part1())


if __name__ == "__main__":
    main()
