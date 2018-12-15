from src.models.dimension import Category
import unittest


class TestCategory(unittest.TestCase):

    def test_properties(self):
        id = 'ID0'
        index = 4
        label = 'label with text'

        category = Category(id, index,  label)
        self.assertEqual(category.id, id)
        self.assertEqual(category.index, index)
        self.assertEqual(category.label, label)
