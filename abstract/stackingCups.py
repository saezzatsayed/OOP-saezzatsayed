from classes import Item, ItemList

num_items = int(input())
item_list = ItemList()

for i in range(num_items):
    line = input().split()
    if line[0].isdigit():
        item = Item(int(line[0]), line[1])
    else:
        item = Item(2 * int(line[1]), line[0])
    item_list.add_item(item)

item_list.sort_items()
item_list.print_items()