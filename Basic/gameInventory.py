#! /usr/bin/python
# gameInventory.py - Display all the items in the inventory before & after updated
iniInv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inventory):
    total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total += v
    print("Total number of items: " + str(total))


def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1
    return inventory


print("Initial Inventory:")
displayInventory(iniInv)

latestInv = addToInventory(iniInv, dragonLoot)

print("Updated Inventory after a vanquished dragon loot:")
displayInventory(latestInv)
