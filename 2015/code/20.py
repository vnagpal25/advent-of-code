import os
import math

day = os.path.basename(__file__).split(".")[0]


def get_factors(n):
    # small factors are all <= sqrt(n)
    small_factors = [x for x in range(1, int(math.sqrt(n)) + 1) if n % x == 0]
    large_factors = [n // small for small in small_factors if small * small != n]

    return small_factors + large_factors


def part1(puzzle):
    input = int(puzzle)
    i = 1
    while True:
        factors = get_factors(i)
        if 10 * sum(factors) >= input:
            return i
        i += 1


def part2(puzzle):
    input = int(puzzle)
    i = 1
    while True:
        factors = get_factors(i)
        # elves only deliver to their first 50 multiples
        if 11 * sum(factor for factor in factors if i / factor <= 50) >= input:
            return i
        i += 1


def main():

    with open(f"../data/{day}/input.txt", "r") as f:
        input = f.read().strip()

    print(f"{'='*60}")
    print("Part 1")
    print(part1(input))

    print(f"{'='*60}")
    print("Part 2")
    print(part2(input))


if __name__ == "__main__":
    main()
