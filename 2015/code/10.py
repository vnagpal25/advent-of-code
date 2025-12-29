import os

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def seq_counter(string):
    string = list(string)

    chunks = []
    chunk = string[0]
    for char in string[1:]:
        if char == chunk[-1]:
            chunk += char
        else:
            chunks.append(chunk)
            chunk = char
    chunks.append(chunk)
    counter = [(chunk[0], len(chunk)) for chunk in chunks]
    return counter


def part1(puzzle: str, n):
    for _ in range(n):
        counter = seq_counter(puzzle)
        puzzle = "".join(str(count) + num for num, count in counter)

    return len(puzzle)

def main():
    with open(f"../data/{day}/sample.txt", "r") as f:
        sample = f.read().strip()
    with open(f"../data/{day}/input.txt", "r") as f:
        input = f.read().strip()

    print(f"{'='*60}")
    print("Part 1")
    if SAMPLE:
        print(part1(sample, 5))
    if PUZZLE:
        print(part1(input, 40))

    print(f"{'='*60}")
    print("Part 2")
    if PUZZLE:
        print(part1(input, 50))


if __name__ == "__main__":
    main()
