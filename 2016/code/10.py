import os
import re
from collections import defaultdict

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def solve(puzzle: str):
    val_assign_pat = r"value (\d+) goes to bot (\d+)"
    val_compare_pat = r"bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)"
    bins = defaultdict(list)
    dag = {}
    outputs = {}
    for line in puzzle.splitlines():
        if re.match(val_assign_pat, line):
            val, bot = re.findall(val_assign_pat, line)[0]
            bins[f"bot_{bot}"].append(int(val))
        elif re.match(val_compare_pat, line):
            source, out1_type, out1_num, out2_type, out2_num = re.findall(
                val_compare_pat, line
            )[0]
            if out1_type == "output":
                outputs[f"{out1_type}_{out1_num}"] = None
            if out2_type == "output":
                outputs[f"{out2_type}_{out2_num}"] = None
            dag[source] = (f"{out1_type}_{out1_num}", f"{out2_type}_{out2_num}")

    while not all(outputs.values()):
        for bot, outs in dag.items():
            if len(bins[f"bot_{bot}"]) < 2:
                continue

            lo, hi = sorted(bins[f"bot_{bot}"])
            bins[f"bot_{bot}"] = []
            if (lo, hi) == (17, 61):
                print(f"Bot {bot} compares 17 and 61")
            if outs[0].startswith("output"):
                outputs[outs[0]] = lo
            else:
                bins[outs[0]].append(lo)

            if outs[1].startswith("output"):
                outputs[outs[1]] = hi
            else:
                bins[outs[1]].append(hi)

    return outputs["output_0"] * outputs["output_1"] * outputs["output_2"]


def part2(puzzle: str): ...


def main():
    with open(f"../data/{day}/sample.txt", "r") as f:
        sample = f.read().strip()
    with open(f"../data/{day}/input.txt", "r") as f:
        input = f.read().strip()

    print(f"{'='*60}")
    print("Part 1 and 2")
    if SAMPLE:
        print(f"Sample input: {solve(sample)}")
    if PUZZLE:
        print(f"Puzzle input: {solve(input)}")

    print(f"{'='*60}")


if __name__ == "__main__":
    main()
