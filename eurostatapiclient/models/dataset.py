from .dimension import ItemList
from functools import reduce
from ..utils.property_decorators import property_is_string,\
    property_is_datetime
from .dimension import Dimension
from datetime import datetime
import pandas as pd


def dimension_list_size(item_list):
    """Compute the total size of an dimension list.

    Parameters
    ----------
    item_list : ItemList
        The Dimension List to compute the size of.

    Returns
    -------
    Integer
        Size of the passed Dimension List

    """
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

    @property
    def dimensions(self):
        return self._dimensions

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
        return dimension_list_size(self._dimensions)

    def add_values(self, value_dict):
        """Add list of value to the dataset object.

        Parameters
        ----------
        value_dict : type
            Dictionary of values

        Returns
        -------
        None

        """
        if not isinstance(value_dict, dict):
            raise ValueError("value_dict must be an instance of Dictonary")

        elif len(value_dict.items()) == self.total_size:
            self._values = [v for k, v in value_dict.items()]

        else:
            values = []
            for i in range(self.total_size):
                v = value_dict.get(str(i), None)
                values.append(v)
            self._values = values

    @classmethod
    def create_from_json(cls, json):
        """Create set from json.

        Parameters
        ----------
        json : type
            Json containing the dataset object.

        Returns
        -------
        Dataset
            Return dataset
        """
        extension = json.get('extension')
        if not (extension and isinstance(extension, dict)):
            raise ValueError("Json is not conformed. \
            Malformed extension field")

        if not json.get("class") == 'dataset':
            raise ValueError("Json is not conformed. \
            Class field is not defined or value not equal to dataset")

        id = extension.get("datasetId")
        version = json.get("version")
        lang = extension.get("lang")
        source = json.get("source")
        updated_raw = json.get("updated")
        updated = datetime.strptime(updated_raw, '%Y-%m-%d')
        label = json.get("label")
        dataset = cls(
            id,
            version,
            lang,
            source,
            updated,
            label
        )

        ids = json.get('id')
        if not (ids and isinstance(ids, list)):
            raise ValueError("Json is not conformed. \
            Dimensions are not defined.")

        sizes = json.get('size')
        dimensions = json.get('dimension')
        for k, v in zip(range(len(ids)), ids):
            dimension = Dimension.create_from_json(
                v,
                k,
                sizes[k],
                dimensions.get(v)
            )
            dataset.add_dimension(dimension)
        values = json.get('value')
        dataset.add_values(values)
        return dataset

    def to_dataframe(self):
        """Convert dataset to a pandas dataframe object.

        Returns
        -------
        Dataframe
            Dataframe reprentation
        """
        dataframe = pd.DataFrame()
        dataframe['values'] = self._values
        for dimension in self.dimensions:
            labels = list(map(lambda c: c.id, dimension.categories))
            self.dimensions[(dimension.index + 1):]
            repeat_elements = dimension_list_size(
                ItemList(self.dimensions[(dimension.index + 1):])
                )
            repeat_blocks = dimension_list_size(
                ItemList(self.dimensions[:dimension.index]))
            labels_block = []
            for l in labels:
                labels_block += [l]*repeat_elements
            dataframe[dimension.id] = labels_block * repeat_blocks
        return dataframe
