from classes import Item, ItemList

def main():
    """
    Main function to process user input, create items, add them to the item list,
    sort the items, and print them.
    """
    num_items = int(input("Enter the number of items: "))
    item_list = ItemList()

    for i in range(num_items):
        line = input("Enter item details (quantity name or name quantity): ").split()
        if line[0].isdigit():
            item = Item(int(line[0]), line[1])
        else:
            item = Item(2 * int(line[1]), line[0])
        item_list.add_item(item)

    item_list.sort_items()
    item_list.print_items()
    print("This file is being run directly")


if __name__ == '__main__':
    main()
else:
    print("This is an imported file")
