import os
from collections import deque

day = os.path.basename(__file__).split(".")[0]

SAMPLE = False
PUZZLE = True


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def part1(puzzle: str):
    gates = deque()
    for line in puzzle.splitlines():
        source, target = line.split(" -> ")
        source = source.split()
        target = target.strip()
        gates.append((source, target))

    values = {}
    while gates:
        source, target = gates.popleft()
        if len(source) == 1:
            value = source[0]
            if isint(value) or value in values:
                if value in values:
                    values[target] = values[value]
                else:
                    values[target] = int(value)
                continue
        elif len(source) == 2:
            # not gate
            if source[1] in values:
                value = values[source[1]]
                values[target] = (~value) & 0xFFFF
                continue
        elif len(source) == 3:
            x, op, y = source
            if (isint(x) or x in values) and (isint(y) or y in values):
                if x in values:
                    x = values[x]
                else:
                    x = int(x)

                if y in values:
                    y = values[y]
                else:
                    y = int(y)

                if op == "AND":
                    values[target] = x & y
                elif op == "OR":
                    values[target] = x | y
                elif op == "LSHIFT":
                    values[target] = x << y
                else:
                    values[target] = x >> y
                continue
        gates.append((source, target))
    return values["a"]


def main():
    with open(f"../data/{day}/sample.txt", "r") as f:
        sample = f.read().strip()
    with open(f"../data/{day}/input.txt", "r") as f:
        input = f.read().strip()
    with open(f"../data/{day}/input2.txt", "r") as f:
        input2 = f.read().strip()
    print(f"{'='*60}")
    print("Part 1")
    if SAMPLE:
        print(part1(sample))
    if PUZZLE:
        print(part1(input))

    print(f"{'='*60}")
    print("Part 2")
    if PUZZLE:
        print(part1(input2))


if __name__ == "__main__":
    main()
