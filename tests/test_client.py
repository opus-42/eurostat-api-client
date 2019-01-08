import unittest
import requests_mock
from eurostatapiclient import EurostatAPIClient

import json
import os

TEST_ASSET_DIR = os.path.join(os.path.dirname(__file__), 'assets')
API_RESPONSE = os.path.join(TEST_ASSET_DIR, 'api_response.json')

VALUES = [8996.6, 9268.3, 295896.6, 310128.7, 12968.9,
          13411.8, 365100.5, 379106.3, 38230.5, 41292,
          441085.7, 504020.9, 19299.5, 19731,
          156718.2, 164040.5, 2580060, 2703120,
          243165.4, 247879.9, 9491671.6, 9754126.3,
          9361942.9, 9603364.1, 9552204.5, 9805603.8,
          14716.5, 16667.6, 226031.4, 207028.9,
          1080935, 1070449, 11825125.1, 12151584.3,
          10990991.1, 11322565.9, 12841529.7,
          13217466.1, 187100, 196869, 1995289,
          2058369, 45155.5, 44825.5, 98826, 101317,
          167721.2, 171140.2, 10332.4, 10889,
          1604514.5, 1637462.9, None, None, 28027.7,
          31275.3, 40177.8, 43164.6, 17788.6, 20202.3,
          3125.1, 3264.8, 7108.3, 7544.2, 6599.5,
          6835.4, 639187, 650359, 324043.2, 358733.7,
          361803.9, 380241.7, 179929.8, 176166.6,
          125408.8, 131925.4, 31545.8, 35431.7,
          369478.2, 405440.1, 36252.4, 36896.3,
          67577.3, 70627.2, 581023.8, 596491.2,
          1850538.6, 1894900.2, 4402, 4814.5]


class TestClient(unittest.TestCase):
    """ Test client """

    def test_client_request(self):
        client = EurostatAPIClient('v2.1', 'json', 'en')
        client.BASE_URL = 'mock://eurostat/wdds/rest/data'
        adapter = requests_mock.Adapter()
        client.session.mount('mock', adapter)

        with open(API_RESPONSE, 'r') as f:
            api_response = json.load(f)

        adapter.register_uri(
            'GET',
            'mock://eurostat/wdds/rest/data/v2.1/json/en/test',
            json=api_response)
        dataset = client.get_dataset('test')
        self.assertEqual(dataset._values, VALUES)
