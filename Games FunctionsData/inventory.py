def displayInventory(inventory):
    print("Inventory:")
    total_items = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        total_items += count
    print(f"Total number of items: {total_items}")

# Example usage
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(inventory)



def addToInventory(inventory, addItems):
    for item in addItems:

        if item in inventory:
            inventory[item] += 1

        else:
            inventory[item] = 1

    return inventory


inventory = {'gold coin': 42, 'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inventory = addToInventory(inventory, dragonLoot)


def displayInventory(inventory):
    print("Inventory:")
    total_items = 0

    for item, count in inventory.items():
        print(f"{count} {item}")
        total_items += count
    print(f"Total number of items: {total_items}")

displayInventory(inventory)