import os
from itertools import product
import math

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = False


def part1():
    # (hp, damage, armor)
    enemy = (100, 8, 2)
    # (cost, damage, armor)
    weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
    armors = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5), None]
    rings = [
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3),
        None,
    ]

    # iterate over cartesian product
    min_cost_to_win = float("inf")
    max_cost_to_lose = float("-inf")
    for weapon, armor, ring1, ring2 in product(weapons, armors, rings, rings):
        # both rings can't be the same
        if ring1 and ring1 == ring2:
            continue
        # calculate cost and armor
        cost = weapon[0]
        armor_hp = 0
        attack = weapon[1]
        if armor:
            cost += armor[0]
            armor_hp += armor[2]
        if ring1:
            cost += ring1[0]
            attack += ring1[1]
            armor_hp += ring1[2]

        if ring2:
            cost += ring2[0]
            attack += ring2[1]
            armor_hp += ring2[2]

        player_attack = max(1, attack - enemy[2])
        enemy_attack = max(1, enemy[1] - armor_hp)

        enemy_turns = math.ceil(100 / enemy_attack)
        my_turns = math.ceil(100 / player_attack)

        if my_turns <= enemy_turns:
            min_cost_to_win = min(min_cost_to_win, cost)
        else:
            max_cost_to_lose = max(max_cost_to_lose, cost)

    return min_cost_to_win, max_cost_to_lose


def main():

    print(f"{'='*60}")
    print("Part 1")
    part1_ans, part2_ans = part1()
    print(part1_ans)

    print(f"{'='*60}")
    print("Part 2")
    print(part2_ans)


if __name__ == "__main__":
    main()
