import os

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def solve(puzzle: str):
    messages = puzzle.splitlines()
    message_len = len(messages[0])
    counts = [[0] * 26 for _ in range(message_len)]

    for message in messages:
        for i, ch in enumerate(message):
            counts[i][ord(ch) - ord("a")] += 1

    max_message = ""
    min_message = ""
    for table in counts:
        max_char = ord("a") + table.index(max(table))
        min_count, min_char = float("inf"), 0
        for ind, count in enumerate(table):
            if not count:
                continue
            if count < min_count:
                min_count = count
                min_char = ord("a") + ind

        max_message += chr(max_char)
        min_message += chr(min_char)

    return max_message, min_message


def part2(puzzle: str): ...


def main():
    with open(f"../data/{day}/sample.txt", "r") as f:
        sample = f.read().strip()
    with open(f"../data/{day}/input.txt", "r") as f:
        input = f.read().strip()

    print(f"{'='*60}")
    print("Part 1")
    sample_part1, sample_part2 = solve(sample)
    puzzle_part1, puzzle_part2 = solve(input)
    print(f"Sample input: {sample_part1}")
    print(f"Puzzle input: {puzzle_part1}")

    print(f"{'='*60}")
    print("Part 2")
    print(f"Sample input: {sample_part2}")
    print(f"Puzzle input: {puzzle_part2}")


if __name__ == "__main__":
    main()
