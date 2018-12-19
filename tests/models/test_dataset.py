from src.models.dataset import dimension_list_size
from src.models.dimension import ItemList, Dimension
import unittest


class DimensionListSizeTest(unittest.TestCase):
    """Unit test for the Dimension List Size Calculations."""

    def test_size_computation(self):
        item_list = ItemList()
        self.assertEqual(dimension_list_size(item_list), 1)
        dimension1 = Dimension('1', 4, 'label1', 2)
        item_list.append(dimension1)
        self.assertEqual(dimension_list_size(item_list), 2)
        dimension2 = Dimension('1', 4, 'label1', 7)
        item_list.append(dimension2)
        self.assertEqual(dimension_list_size(item_list),14)
