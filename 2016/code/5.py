import os
from hashlib import md5
from functools import cache

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


@cache
def cache_hash(to_encode):
    return md5(to_encode.encode("utf-8"))


def part1(puzzle: str):
    i = 0
    password = ""
    while len(password) < 8:
        to_encode = f"{puzzle}{i}"
        # Encode the string to bytes and calculate the MD5 hash
        md5_hash_object = cache_hash(to_encode)
        hex_digest = md5_hash_object.hexdigest()

        if hex_digest.startswith("00000"):
            password += str(hex_digest[5])

        i += 1
    return password


def part2(puzzle: str):
    i = 0
    password = ["_"] * 8
    while any(digit == "_" for digit in password):
        to_encode = f"{puzzle}{i}"
        # Encode the string to bytes and calculate the MD5 hash
        md5_hash_object = cache_hash(to_encode)
        hex_digest = md5_hash_object.hexdigest()

        if hex_digest.startswith("00000"):
            pos = int(hex_digest[5], 16)
            if 0 > pos or pos > 7 or password[pos] != "_":
                i += 1
                continue
            password[pos] = hex_digest[6]
            print("".join(password))

        i += 1
    return "".join(password)


def main():
    with open(f"../data/{day}/sample.txt", "r") as f:
        sample = f.read().strip()
    with open(f"../data/{day}/input.txt", "r") as f:
        input = f.read().strip()

    print(f"{'='*60}")
    print("Part 1")
    if SAMPLE:
        print(f"Sample input: {part1(sample)}")
    if PUZZLE:
        print(f"Puzzle input: {part1(input)}")

    print(f"{'='*60}")
    print("Part 2")
    if SAMPLE:
        print(f"Sample input: {part2(sample)}")
    if PUZZLE:
        print(f"Puzzle input: {part2(input)}")


if __name__ == "__main__":
    main()
