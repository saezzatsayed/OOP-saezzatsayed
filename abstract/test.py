import unittest
import coverage
from classes import Item, ItemList
from hypothesis import given
from hypothesis import strategies as st

# Create a coverage object
cov = coverage.Coverage()
cov.start()

class ItemTests(unittest.TestCase):
    def test_get_quantity(self):
        item = Item(10, "Red")
        self.assertEqual(item.get_quantity(), 10)

    def test_set_quantity(self):
        item = Item(10, "Red")
        item.set_quantity(5)
        self.assertEqual(item.get_quantity(), 5)

    def test_get_name(self):
        item = Item(10, "Red")
        self.assertEqual(item.get_name(), "Red")

    def test_set_name(self):
        item = Item(10, "Red")
        item.set_name("Blue")
        self.assertEqual(item.get_name(), "Blue")

class ItemListTests(unittest.TestCase):
    def test_add_item(self):
        item_list = ItemList()
        item = Item(10, "Red")
        item_list.add_item(item)
        self.assertEqual(len(item_list._items), 1)

    def test_sort_items(self):
        item_list = ItemList()
        item1 = Item(10, "Red")
        item2 = Item(5, "Blue")
        item_list.add_item(item1)
        item_list.add_item(item2)
        item_list.sort_items()
        self.assertEqual(item_list._items[0].get_quantity(), 5)
        self.assertEqual(item_list._items[1].get_quantity(), 10)


    @given(st.integers(min_value=0), st.text())
    def test_add_item_property(self, quantity, name):
        item_list = ItemList()
        item = Item(quantity, name)
        item_list.add_item(item)
        self.assertIn(item, item_list._items)

if __name__ == '__main__':
    # Stop the code coverage measurement
    cov.stop()
    # Generate the HTML report
    cov.html_report(directory='coverage_report')
    # Run the tests
    unittest.main()
