from random import randint

inventory = {}
party = []

def throw_dice(msg):
    results = []
    
    die_array = msg.split("d")
    if die_array[0] == "":
        die_array[0] = 1
    for x in range(1, int(die_array[0]) + 1):
        results.append(randint(0,int(die_array[1])))
    print(results)
    return results


def add_to_inventory(msg):
    arguments = msg.split(" ")
    user = arguments[0]
    item = arguments[1]

    if not user in inventory:
        inventory[user] = []
        
    inventory[user].append(item)    
    
def show_inventory(user):
    if not user in inventory:
        inventory[user] = []

    return inventory[user]

def delete_from_inventory(msg):
    arguments = msg.split(" ")
    user = arguments[0]
    item = arguments[1]

    if not user in inventory:
        inventory[user] = []

    if not item in inventory[user]:
        return "The object does not exist"
    else:
        inventory[user].remove(item)

#def add_party_member(msg):

# print(throw_dice("d4"))
# print(throw_dice("4d10"))
# print(throw_dice("1d20"))

# print(show_inventory("Otarin"))
# print(add_to_inventory("Otarin Cheese"))
# print(show_inventory("Otarin"))
# print(delete_from_inventory("Otarin Cheese"))
# print(show_inventory("Otarin"))
