import os

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def custom_range(i, j):
    if i < j:
        return range(i, j)[1:]
    else:
        return range(i, j, -1)[1:]


def part1(puzzle: str):
    curr = (0, 0)
    dir = (-1, 0)  # north

    for inst in puzzle.split(", "):
        dist = int(inst[1:])
        if inst[0] == "L":
            dir = (-dir[1], dir[0])
        elif inst[0] == "R":
            dir = (dir[1], -dir[0])
        curr = (curr[0] + dist * dir[0], curr[1] + dist * dir[1])
    return sum(map(abs, curr))


def part2(puzzle: str):
    curr = (0, 0)
    dir = (-1, 0)  # north
    visited = {(0, 0)}
    for inst in puzzle.split(", "):
        dist = int(inst[1:])
        if inst[0] == "L":
            dir = (-dir[1], dir[0])
        elif inst[0] == "R":
            dir = (dir[1], -dir[0])
        next = (curr[0] + dist * dir[0], curr[1] + dist * dir[1])
        if curr[0] == next[0]:
            intermediates = [(curr[0], c) for c in custom_range(curr[1], next[1] + 1)]
        else:
            intermediates = [(r, curr[1]) for r in custom_range(curr[0], next[0] + 1)]
        curr = next
        if set(intermediates) & visited:
            for loc in intermediates:
                if loc in visited:
                    return sum(map(abs, loc))
        visited |= set(intermediates)


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
