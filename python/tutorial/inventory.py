# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'rope': 1, 'gold coin': 42}

def addToInventory(inventory, addedItems):
    for item in addedItems:
        curItemCount = inventory.get(item, 0)
        if curItemCount == 0:
            inv[item] = 1
        else:
            inv[item] += 1

def displayInventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items: '+ str(item_total))

displayInventory(inv)
print('-------')
addToInventory(inv, dragonLoot)
print('Looting dragon...')
print('-------')
displayInventory(inv)
