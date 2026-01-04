import os
from collections import namedtuple
from copy import deepcopy

day = os.path.basename(__file__).split(".")[0]

SAMPLE = True
PUZZLE = False


def answer():

    Spell = namedtuple("spell", "name, cost, damage, heal, armor, mana, duration")
    spells = {
        Spell("missile", 53, 4, 0, 0, 0, 0),
        Spell("drain", 73, 2, 2, 0, 0, 0),
        Spell("shield", 113, 0, 0, 7, 0, 6),
        Spell("poison", 173, 3, 0, 0, 0, 6),
        Spell("recharge", 229, 0, 0, 0, 101, 5),
    }

    # boss inputs
    BOSS_DMG = 8
    BOSS_HP = 55

    def battle(hard_mode=False):
        def apply_effects(s, boss_turn=False):
            for spell in s["active_spells"]:
                s["boss_hp"] -= spell.damage
                s["mana"] += spell.mana
                s["hp"] += spell.heal
                if spell.armor > 0 and boss_turn:
                    s["hp"] += 7
            s["active_spells"] = {
                spell: dur - 1 for spell, dur in s["active_spells"].items() if dur > 1
            }

        # our initial state is having 500 mana and full health
        states = [
            {
                "mana": 500,
                "hp": 50,
                "boss_hp": BOSS_HP,
                "active_spells": dict(),
                "spent_mana": 0,
            }
        ]
        result = float("inf")
        while states:
            s = states.pop()
            s["hp"] -= hard_mode
            # if the player is dead, we don't consider it
            if s["hp"] <= 0:
                continue
            apply_effects(s)
            # if the boss dies, we record the spent mana
            if s["boss_hp"] <= 0:
                result = min(result, s["spent_mana"])
                continue
            for spell in spells:
                if (
                    spell.cost <= s["mana"]
                    and s["spent_mana"] + spell.cost < result
                    and spell not in s["active_spells"]
                ):
                    new_s = deepcopy(s)
                    new_s["mana"] -= spell.cost
                    new_s["spent_mana"] += spell.cost
                    new_s["active_spells"][spell] = spell.duration
                    apply_effects(new_s, boss_turn=True)
                    if new_s["boss_hp"] <= 0:
                        result = min(result, new_s["spent_mana"])
                        continue
                    new_s["hp"] -= BOSS_DMG
                    if new_s["hp"] > 0:
                        states.append(new_s)
        return result

    return battle(), battle(True)


def main():
    print(f"{'='*60}")
    print("Part 1")
    print(answer()[0])

    print(f"{'='*60}")
    print("Part 2")
    print(answer()[1])


if __name__ == "__main__":
    main()
