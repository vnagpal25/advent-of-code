import os

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def part1(puzzle: str):
    pad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

    def direction(dir):
        if dir == "U":
            return (-1, 0)
        elif dir == "L":
            return (0, -1)
        elif dir == "D":
            return (1, 0)
        elif dir == "R":
            return (0, 1)

    code = ""
    curr = [1, 1]
    for inst in puzzle.splitlines():
        moves = list(map(direction, list(inst)))
        for dr, dc in moves:
            if dr:
                # up or down
                curr[0] += dr
                curr[0] = min(2, max(0, curr[0]))
            elif dc:
                # right or left
                curr[1] += dc
                curr[1] = min(2, max(0, curr[1]))

        code += pad[curr[0]][curr[1]]

    return code


def part2(puzzle: str):
    pad = [
        [None, None, "1", None, None],
        [None, "2", "3", "4", None],
        ["5", "6", "7", "8", "9"],
        [None, "A", "B", "C", None],
        [None, None, "D", None, None],
    ]

    def direction(dir):
        if dir == "U":
            return (-1, 0)
        elif dir == "L":
            return (0, -1)
        elif dir == "D":
            return (1, 0)
        elif dir == "R":
            return (0, 1)

    code = ""
    curr = [2, 0]
    for inst in puzzle.splitlines():
        moves = list(map(direction, list(inst)))
        for dr, dc in moves:
            if dr and 0 <= curr[0] + dr <= 4 and pad[curr[0] + dr][curr[1]]:
                # up or down
                curr[0] += dr
            elif dc and 0 <= curr[1] + dc <= 4 and pad[curr[0]][curr[1] + dc]:
                # right or left
                curr[1] += dc

        code += pad[curr[0]][curr[1]]

    return code


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
