import request
from .utils.property_decorators import property_is_string


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
    def api_url():
        return '{0}/{1}/{2}'.format(BASE_URL, version, json, en)

    def get_dataset(id, params={}):
        pass
