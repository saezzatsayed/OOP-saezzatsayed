from abc import ABC
from typing import List
from io import StringIO

class Item(ABC):
    def __init__(self, quantity: int, name: str):
        """
        Initializes an Item object with a quantity and name.

        Args:
            quantity (int): The quantity of the item.
            name (str): The name of the item.
        """
        super().__init__()
        self._quantity = quantity
        self._name = name

    def get_quantity(self) -> int:
        """
        Returns the quantity of the item.

        Returns:
            int: The quantity of the item.
        """
        return self._quantity

    def set_quantity(self, quantity: int):
        """
        Sets the quantity of the item.

        Args:
            quantity (int): The new quantity of the item.
        """
        self._quantity = quantity

    def get_name(self) -> str:
        """
        Returns the name of the item.

        Returns:
            str: The name of the item.
        """
        return self._name

    def set_name(self, name: str):
        """
        Sets the name of the item.

        Args:
            name (str): The new name of the item.
        """
        self._name = name


class ItemList:
    def __init__(self):
        """
        Initializes an ItemList object with an empty list of items.
        """
        self._items = []

    def add_item(self, item: Item):
        """
        Adds an item to the item list.

        Args:
            item (Item): The item to be added to the list.
        """
        self._items.append(item)

    def sort_items(self):
        """
        Sorts the items in the item list based on their quantities.
        """
        self._items = sorted(self._items, key=lambda item: item.get_quantity())

    def print_items(self):
        """
        Prints the names of the items in the item list.
        """
        for item in self._items:
            print(item.get_name())
