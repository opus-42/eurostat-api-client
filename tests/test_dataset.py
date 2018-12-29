from src.models.dataset import dimension_list_size
from src.models.dimension import ItemList, Dimension
import unittest
from src.models.dataset import Dataset
import datetime
import json
import os

TEST_ASSET_DIR = os.path.join(os.path.dirname(__file__), 'assets')
ADD_DATASET = os.path.join(TEST_ASSET_DIR, 'add_dataset.json')


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
        self.assertEqual(dimension_list_size(item_list), 14)


class DatasetUnitTest(unittest.TestCase):
    """Unit test for the Dataset List Size Calculations."""

    def test_dataset_creation(self):
        updated = datetime.datetime(2018, 1, 1)
        dataset = Dataset('id',
                          'v2.0',
                          'FR',
                          'Eurostat',
                          updated,
                          'Some label')
        self.assertEqual(dataset.updated, updated)
        self.assertEqual(dataset.id, 'id')
        self.assertEqual(dataset.version, 'v2.0')
        self.assertEqual(dataset.lang, 'FR')
        self.assertEqual(dataset.label, 'Some label')
        self.assertEqual(dataset.source, 'Eurostat')

    def test_add_values(self):
        updated = datetime.datetime(2018, 1, 1)
        dataset = Dataset('id',
                          'v2.0',
                          'FR',
                          'Eurostat',
                          updated,
                          'Some label')
        dimension1 = Dimension('1', 0, 'label1', 2)
        dimension2 = Dimension('2', 1, 'label2', 5)
        dataset.add_dimension(dimension1)
        dataset.add_dimension(dimension2)
        values = {
            '1': 2,
            '0': 1,
            '2': 1,
            '4': 11,
            '5': 10,
            '6': 2,
            '7': 3,
            '9': 4,
        }
        dataset.add_values(values)
        self.assertEqual(dataset._values[0], 1)
        self.assertEqual(dataset._values[1], 2)
        self.assertEqual(dataset._values[5], 10)
        self.assertEqual(dataset._values[3], None)
        self.assertEqual(dataset._values[8], None)

    def test_dataset_from_json(self):
        with open(ADD_DATASET, 'r') as f:
            dataset_json = json.load(f)

        dataset = Dataset.create_from_json(dataset_json)
        self.assertEqual(dataset.id, 'nama_10_gdp')
        self.assertEqual(dataset.version, '2.0')
        self.assertEqual(dataset.lang, 'EN')
        self.assertEqual(dataset.source, 'Eurostat')
        self.assertEqual(dataset.updated, datetime.datetime(2018, 12, 20))
        label = 'GDP and main components (output, expenditure and income)'
        self.assertEqual(dataset.label, label)
        self.assertEqual(dataset.dimensions.count, 4)
        self.assertEqual(dataset.total_size, 2)
        self.assertEqual(dataset._values, [
            12841529.7,
            13217466.1
        ])
        print(dataset.to_dataframe())
