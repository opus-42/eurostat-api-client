import requests
from .utils.property_decorators import property_is_string
from .models.dataset import Dataset


class EurostatAPIClient(object):
    """Represent an API client that handle Dataset Request
    and return dataset object.

    Parameters
    ----------
    version : String
        version of the API
    response_type : String
        type of file returned (should be 'json')
    language : String
        2 letter code for the language of the label and metadata.
        Should be one of these these : fr, en, de

    Attributes
    ----------
    BASE_URL : String
        Root Url of the Eurostat API
    version
    response_type
    language

    """
    BASE_URL = 'https://ec.europa.eu/eurostat/wdds/rest/data'
    session = requests.Session()

    def __init__(self, version, response_type, language):
        self.version = version
        self.response_type = response_type
        self.language = language
        
    def set_proxy(self, proxy_dict):
        """Set a proxy for the requests.

        For example:
        ```python3
        {
            'http':'http://my.proxy:8080',
            'https':'http://my.proxy:8080'
        }
        ```
        For more information see requests documentation.
        https://2.python-requests.org/en/master/user/advanced/#proxies

        Parameters
        ----------
        proxy_dict : dict
            a dictionary of proxies to any request method
            (see Requests documentation).
        """
        self.session.proxies.update(proxy_dict)

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
        response = self.session.get(request_url, params=params)
        response.raise_for_status()
        return Dataset.create_from_json(response.json())
