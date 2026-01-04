import os

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def part1(puzzle: str, a):
    registers = {"a": a, "b": 0}
    instructions = puzzle.splitlines()
    i = 0
    while i < len(instructions):
        inst = instructions[i].replace(",", "")
        inst = inst.split()
        # print(f"Executing instruction {i}: {inst}")
        # print(registers)
        command = inst[0]
        reg = inst[1]
        if command == "hlf":
            registers[reg] //= 2
        elif command == "tpl":
            registers[reg] *= 3
        elif command == "inc":
            registers[reg] += 1
        else:
            # jump instruction
            if command == "jmp":
                i += int(reg)
            elif command == "jie":
                if registers[reg] % 2 == 0:
                    i += int(inst[2])
                else:
                    i += 1
            elif command == "jio":
                if registers[reg] == 1:
                    i += int(inst[2])
                else:
                    i += 1

            continue
        # not a jump instruction, so continue
        i += 1
    return registers["b"]


def main():
    with open(f"../data/{day}/sample.txt", "r") as f:
        sample = f.read().strip()
    with open(f"../data/{day}/input.txt", "r") as f:
        input = f.read().strip()

    print(f"{'='*60}")
    print("Part 1")
    print(part1(input, 0))

    print(f"{'='*60}")
    print("Part 2")
    print(part1(input, 1))


if __name__ == "__main__":
    main()
