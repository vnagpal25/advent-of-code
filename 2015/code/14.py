import os
import re
import numpy as np
import itertools

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = True


def part1(puzzle: str, t: int):
    pattern = r"\w+ can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
    max_distance = float("-inf")
    for line in puzzle.splitlines():
        distance = 0
        speed, fly_time, rest_time = map(int, re.findall(pattern, line)[0])

        chunk_time = fly_time + rest_time
        num_chunks = t // chunk_time
        distance += speed * fly_time * num_chunks

        remaining = t % chunk_time
        rem_fly_time = min(remaining, fly_time)
        distance += speed * rem_fly_time

        max_distance = max(max_distance, distance)
    return max_distance


def part2(puzzle: str, t: int):
    pattern = r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds."
    history = {}
    for line in puzzle.splitlines():
        reindeer, *physics_info = re.findall(pattern, line)[0]
        speed, fly_time, rest_time = map(int, physics_info)
        steps = itertools.cycle([speed] * fly_time + [0] * rest_time)
        history[reindeer] = list(itertools.accumulate(next(steps) for _ in range(t)))

    points = {}
    leads = [max(curr_distances) for curr_distances in zip(*history.values())]

    for reindeer, distances in history.items():
        for i, dist in enumerate(distances):
            if dist == leads[i]:
                points[reindeer] = points.get(reindeer, 0) + 1

    return max(points.values())


def main():
    with open(f"../data/{day}/sample.txt", "r") as f:
        sample = f.read().strip()
    with open(f"../data/{day}/input.txt", "r") as f:
        input = f.read().strip()

    print(f"{'='*60}")
    print("Part 1")
    if SAMPLE:
        print(part1(sample, 1000))
    if PUZZLE:
        print(part1(input, 2503))

    print(f"{'='*60}")
    print("Part 2")
    if SAMPLE:
        print(part2(sample, 1000))
    if PUZZLE:
        print(part2(input, 2503))


if __name__ == "__main__":
    main()
