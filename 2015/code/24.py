import os

day = os.path.basename(__file__).split(".")[0]

SAMPLE = False
PUZZLE = True


def part1(puzzle: str):
    presents = sorted(map(int, puzzle.splitlines()), reverse=True)
    goal = sum(presents) / 3
    # we store the configurations of all possible valid first groups
    possible_solutions = set()

    def aux(remaining, score, used, qe):
        if score == goal:
            # found valid
            possible_solutions.add((used, qe))
        elif score < goal and remaining and used < 6:
            # skip next one
            aux(remaining[1:], score, used, qe)
            # include next one
            aux(remaining[1:], score + remaining[0], used + 1, qe * remaining[0])

    aux(presents, 0, 0, 1)
    return min(possible_solutions)[1]


def part2(puzzle: str):
    presents = sorted(map(int, puzzle.splitlines()), reverse=True)
    goal = sum(presents) / 4
    # we store the configurations of all possible valid first groups
    possible_solutions = set()

    def aux(remaining, score, used, qe):
        if score == goal:
            # found valid
            possible_solutions.add((used, qe))
        elif score < goal and remaining and used < 6:
            # skip next one
            aux(remaining[1:], score, used, qe)
            # include next one
            aux(remaining[1:], score + remaining[0], used + 1, qe * remaining[0])

    aux(presents, 0, 0, 1)
    return min(possible_solutions)[1]


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
