import requests
from .utils.property_decorators import property_is_string
from .models.dataset import Dataset


class EurostatAPIClient(object):
    BASE_URL = 'https://ec.europa.eu/eurostat/wdds/rest/data'

    def __init__(self, version, response_type, language):
        self.version = version
        self.response_type = response_type
        self.language = language

    @property
    def version(self):
        return self._version

    @version.setter
    @property_is_string
    def version(self, value):
        self._version = value

    @property
    def response_type(self):
        return self._response_type

    @response_type.setter
    @property_is_string
    def response_type(self, value):
        self._response_type = value

    @property
    def language(self):
        return self._language

    @language.setter
    @property_is_string
    def language(self, value):
        self._language = value

    @property
    def api_url(self):
        return '{0}/{1}/{2}/{3}'.format(self.BASE_URL,
                                        self.version,
                                        self.response_type,
                                        self.language)

    def get_dataset(self, id, params={}):
        request_url = '{0}/{1}'.format(self.api_url, id)
        response = requests.get(request_url, params=params)
        response.raise_for_status()
        return Dataset.create_from_json(response.json())
