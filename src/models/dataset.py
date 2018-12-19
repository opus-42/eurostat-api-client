from .dimension import ItemList
from functools import reduce
from src.utils.property_decorators import property_is_string,\
    property_is_datetime


def dimension_list_size(item_list):
    if item_list.count == 0:
        return 1
    elif item_list.count == 1:
        return item_list[0].size
    else:
        return reduce(lambda x, y: x * y, [i.size for i in item_list])


class Dataset(object):
    """Short summary.

    Parameters
    ----------
    id : Stringtype
        Unique Id of the dataset within Eurostat
    version : String
        Version of the dataset
    lang : String
        Language used in the dataset labels and metadata
    source : String
        Source of the dataset. Should be something like "Eurostat"
    updated : Datetime
        Last time the dataset was updated. This is typically a date.
    label : String
        Label of the dataset

    Attributes
    ----------
    values : List
        List of values
    dimensions : ItemList
        List of dimensions of the dataset

    id
    version
    lang
    source
    updated
    label

    """

    def __init__(self, id, version, lang, source, updated, label):
        self.id = id
        self.version = version
        self.lang = lang
        self.source = source
        self.updated = updated
        self.label = label
        self._values = []
        self._dimensions = ItemList()

    @property
    def id(self):
        return self._id

    @id.setter
    @property_is_string
    def id(self, value):
        self._id = value

    @property
    def version(self):
        return self._version

    @version.setter
    @property_is_string
    def version(self, value):
        self._version = value

    @property
    def lang(self):
        return self._lang

    @lang.setter
    @property_is_string
    def lang(self, value):
        self._lang = value

    @property
    def source(self):
        return self._source

    @source.setter
    @property_is_string
    def source(self, value):
        self._source = value

    @property
    def updated(self):
        return self._updated

    @updated.setter
    @property_is_datetime
    def updated(self, value):
        self._updated = value

    @property
    def label(self):
        return self._label

    @label.setter
    @property_is_string
    def label(self, value):
        self._label = value

    def add_dimension(self, dimension):
        """Add a dimension to the dataset

        Parameters
        ----------
        dimension : Dimension
            Dimension to add to the list of dimensions

        Returns
        -------
        None

        """

        # TO DO : there may be some position checks to add
        self._dimensions.append(dimension)

    @property
    def total_size(self):
        pass
