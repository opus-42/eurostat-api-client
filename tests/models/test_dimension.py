from src.models.dimension import Category, BaseItem, ItemList, \
    Dimension
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


class TestBaseItem(unittest.TestCase):

    def test_properties(self):
        id = 'ID0'
        index = 4
        label = 'label with text'

        category = BaseItem(id, index,  label)
        self.assertEqual(category.id, id)
        self.assertEqual(category.index, index)
        self.assertEqual(category.label, label)

    def test_item_list_assignation(self):
        item_list = ItemList()
        self.assertRaises(ValueError, item_list.__setitem__, 0, 'd')

    def test_item_list_count(self):
        item_list = ItemList()
        self.assertEqual(len(item_list), 0)
        self.assertEqual(item_list.count, 0)
        category1 = BaseItem('id', 0,  'label')
        category2 = BaseItem('id', 1,  'label')
        item_list.append(category1)
        item_list.append(category2)
        self.assertEqual(len(item_list), 2)
        self.assertEqual(item_list.count, 2)


class TestDimension(unittest.TestCase):

    def test_add_category(self):
        id = 'ID0'
        index = 4
        label = 'label with text'
        dimension = Dimension(id, index, label)
        category = Category(id, index,  label)
        self.assertEqual(dimension.categories.count, 0)
        dimension.add_category(category)
        self.assertEqual(dimension.categories.count, 1)

    def test_create_from_json(self):
        json = {
            'label': "time",
            'category':	{
                'index': {
                    '2010':	'1',
                    '2011':	'0'
                },
                'label': {
                    '2010':	'2010',
                    '2011':	'test'
                },
            }
        }
        id = 'ID0'
        index = 4
        label = 'time'

        dimension = Dimension.create_from_json(id, index, json)
        self.assertEqual(dimension.categories.count, 2)
        self.assertEqual(dimension.label, label)
        self.assertEqual(dimension.categories[0].label, 'test')
