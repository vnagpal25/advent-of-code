import os
import hashlib

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def part1(puzzle: str):
    i = 1
    while True:
        to_encode = f"{puzzle}{i}"

        # Encode the string to bytes and calculate the MD5 hash
        md5_hash_object = hashlib.md5(to_encode.encode("utf-8"))
        hex_digest = md5_hash_object.hexdigest()

        if hex_digest.startswith("00000"):
            return i

        i += 1


def part2(puzzle: str):
    i = 1
    while True:
        to_encode = f"{puzzle}{i}"

        # Encode the string to bytes and calculate the MD5 hash
        md5_hash_object = hashlib.md5(to_encode.encode("utf-8"))
        hex_digest = md5_hash_object.hexdigest()

        if hex_digest.startswith("000000"):
            return i

        i += 1


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
