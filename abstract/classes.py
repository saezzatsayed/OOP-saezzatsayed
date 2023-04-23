class Item:
    def __init__(self, quantity, name):
        self._quantity = quantity
        self._name = name

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity):
        self._quantity = quantity

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


class ItemList:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def sort_items(self):
        self._items = sorted(self._items, key=lambda item: item.get_quantity())

    def print_items(self):
        for item in self._items:
            print(item.get_name())
