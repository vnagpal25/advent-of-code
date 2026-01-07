import os
import numpy as np

day = os.path.basename(__file__).split(".")[0]

SAMPLE = False
PUZZLE = True


def part1(puzzle: str):
    grid = np.zeros((6, 50))

    for inst in puzzle.splitlines():
        inst = inst.split()
        if inst[0] == "rect":
            w, h = map(int, inst[1].split("x"))
            grid[:h, :w] = 1
        elif inst[1] == "row":
            # rotate row y=0 by 4
            row = int(inst[2].split("=")[1])
            shift = int(inst[4])
            # shift all column indices
            row_len = len(grid[0])
            indices = [(ind - shift) % row_len for ind in range(row_len)]
            new_row = np.array([grid[row][ind] for ind in indices])
            grid[row] = new_row
        elif inst[1] == "column":
            col = int(inst[2].split("=")[1])
            shift = int(inst[4])
            # shift all column indices
            col_len = len(grid)
            indices = [(ind - shift) % col_len for ind in range(col_len)]
            new_column = [grid[ind][col] for ind in indices]
            grid[:, col] = new_column
    for row in grid:
        row = ["\u2588" if light else "." for light in row]
        row = [char if i % 5 else "_" + char for i, char in enumerate(row)]
        print("".join(row))
    return int(np.sum(grid))


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


if __name__ == "__main__":
    main()
