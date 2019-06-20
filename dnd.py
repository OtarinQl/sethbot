from random import randint

inventory = {}
party = {}


def throw_dice(dice):
    results = []

    die_array = dice.split("d")
    if die_array[0] == "":
        die_array[0] = 1
    for _ in range(1, int(die_array[0]) + 1):
        results.append(randint(1, int(die_array[1])))
    # print(results)
    return results


def add_to_inventory(user, item):
    if not user in inventory:
        inventory[user] = []

    inventory[user].append(item)


def show_inventory(user):
    if not user in inventory:
        inventory[user] = []

    return inventory[user]


def delete_from_inventory(user, item):
    if not user in inventory:
        inventory[user] = []

    if not item in inventory[user]:
        return "The object does not exist"
    else:
        inventory[user].remove(item)
        return item + " has been deleted, **BABY**!"

def add_party_member(name):
    party[name] = {}

def show_party():
    return party.keys()

# print(throw_dice("d4"))
# print(throw_dice("4d10"))
# print(throw_dice("1d20"))

# print(show_inventory("Otarin"))
# print(add_to_inventory("Otarin Cheese"))
# print(show_inventory("Otarin"))
# print(delete_from_inventory("Otarin Cheese"))
# print(show_inventory("Otarin"))
