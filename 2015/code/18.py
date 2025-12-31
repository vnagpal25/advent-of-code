import os
import numpy as np

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def part1(puzzle: str, t):
    grid = [
        [0] + list(map(lambda x: 1 if x == "#" else 0, list(line))) + [0]
        for line in puzzle.splitlines()
    ]
    grid = np.array([[0] * len(grid[0])] + grid + [[0] * len(grid[0])])
    for _ in range(t):
        on = []
        off = []
        for r in range(1, len(grid) - 1):
            for c in range(1, len(grid[r]) - 1):
                tot = sum(
                    grid[r + di][c + dj] for di in (-1, 0, 1) for dj in (-1, 0, 1)
                )
                if grid[r][c]:
                    # on
                    tot -= 1
                    if tot not in [2, 3]:
                        off.append((r, c))
                else:
                    # off
                    if tot == 3:
                        on.append((r, c))
        for r, c in on:
            grid[r][c] = 1
        for r, c in off:

            grid[r][c] = 0

    return np.sum(grid)


def part2(puzzle: str, t):
    grid = [
        [0] + list(map(lambda x: 1 if x == "#" else 0, list(line))) + [0]
        for line in puzzle.splitlines()
    ]
    grid = np.array([[0] * len(grid[0])] + grid + [[0] * len(grid[0])])
    grid[1][1] = 1
    grid[len(grid) - 2][1] = 1
    grid[1][len(grid[0]) - 2] = 1
    grid[len(grid) - 2][len(grid[0]) - 2] = 1
    for _ in range(t):
        on = []
        off = []
        for r in range(1, len(grid) - 1):
            for c in range(1, len(grid[r]) - 1):
                tot = sum(
                    grid[r + di][c + dj] for di in (-1, 0, 1) for dj in (-1, 0, 1)
                )
                if grid[r][c]:
                    # on
                    tot -= 1
                    if tot not in [2, 3]:
                        off.append((r, c))
                else:
                    # off
                    if tot == 3:
                        on.append((r, c))
        for r, c in on:
            grid[r][c] = 1
        for r, c in off:
            if (r, c) in {
                (1, 1),
                (1, len(grid[0]) - 2),
                (len(grid) - 2, 1),
                (len(grid) - 2, len(grid[0]) - 2),
            }:
                continue
            grid[r][c] = 0
    return np.sum(grid)

def main():
    with open(f"../data/{day}/sample.txt", "r") as f:
        sample = f.read().strip()
    with open(f"../data/{day}/input.txt", "r") as f:
        input = f.read().strip()

    print(f"{'='*60}")
    print("Part 1")
    if SAMPLE:
        print(part1(sample, 4))
    if PUZZLE:
        print(part1(input, 100))

    print(f"{'='*60}")
    print("Part 2")
    if SAMPLE:
        print(part2(sample, 5))
    if PUZZLE:
        print(part2(input, 100))


if __name__ == "__main__":
    main()
