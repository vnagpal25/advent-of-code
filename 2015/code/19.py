import os
from collections import defaultdict
import random

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def decode(string: str):
    decoded = []
    for atom in string:
        if atom.islower():
            last = decoded.pop()
            atom = last + atom
        decoded.append(atom)

    return decoded


def part1(puzzle: str):
    rules_strings, molecule = puzzle.split("\n\n")
    molecule = decode(molecule)
    rules = defaultdict(list)
    for rule in rules_strings.splitlines():
        x, y = rule.split(" => ")
        rules[x].append(y)

    possible = set()
    for i, char in enumerate(molecule):
        for replacement in rules[char]:
            temp = list(molecule)
            temp = temp[:i] + list(replacement) + temp[i + 1 :]

            possible.add("".join(temp))

    return len(possible)


def part2(puzzle: str):
    rules_strings, molecule = puzzle.split("\n\n")
    # molecule = tuple(decode(molecule))
    replacements = {}
    for rule in rules_strings.splitlines():
        x, y = rule.split(" => ")
        replacements[y] = x

    count = 0
    while molecule != "e":
        random_molecule = random.choice(list(replacements.keys()))

        if random_molecule in molecule:
            molecule = molecule.replace(
                random_molecule, replacements[random_molecule], 1
            )
            count += 1

    return count


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
    if SAMPLE:
        print("This solution doesn't work for sample input")
    if PUZZLE:
        print(part2(input))


if __name__ == "__main__":
    main()
