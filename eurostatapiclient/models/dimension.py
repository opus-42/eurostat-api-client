from ..utils.property_decorators import property_is_int, property_is_string


class BaseItem(object):
    """Base class defining an Item

    Parameters
    ----------
    id : String
        Unique ID for the item
    index : Integer
        Position of the item within list of similar items.
    label : String
        Explicit label for the item.

    Attributes
    ----------
    id
    index
    label

    """

    def __init__(self, id, index, label):
        self.id = id
        self.index = index
        self.label = label

    @property
    def id(self):
        return self._id

    @id.setter
    @property_is_string
    def id(self, value):
        self._id = value

    @property
    def index(self):
        return self._index

    @index.setter
    @property_is_int()
    def index(self, value):
        self._index = value

    @property
    def label(self):
        return self._label

    @label.setter
    @property_is_string
    def label(self, value):
        self._label = value


class ItemList(list):
    """List of BaseItem (or any sub-class)"""

    def __setitem__(self, key, value):
        if not isinstance(value, BaseItem):
            raise ValueError('Items must be Base Item')
        super.__setitem__(key, value)

    @property
    def count(self):
        return self.__len__()


class Category(BaseItem):
    """Represent a category item with a dimension.

    Parameters
    ----------
    id : String
        See BaseItem for details.
    index : type
        See BaseItem for details.
    label : type
        See BaseItem for details.

    """

    def __init__(self, id, index, label):
        super().__init__(id, index, label)


class Dimension(BaseItem):
    """Represent a dimension item

    Parameters
    ----------
    id : String
        See BaseItem documentation
    index : Integer
        See BaseItem documentation
    label : String
        See BaseItem documentation
    size : Integer
        Size of the dimension

    Attributes
    ----------
    categories : ItemList
        List of categories related to the dimension

    """

    def __init__(self, id, index, label, size):
        super().__init__(id, index, label)
        self.size = size
        self.categories = ItemList()

    @property
    def size(self):
        return self._size

    @size.setter
    @property_is_int()
    def size(self, value):
        self._size = value

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, value):
        self._categories = value

    def add_category(self, category):
        """Add a category to the dimension

        Parameters
        ----------
        category : Category
            Category to add to the list of category

        Returns
        -------
        None

        """

        # TO DO : there may be some position checks to add
        self._categories.append(category)

    @classmethod
    def create_from_json(cls, id, index, size, json):
        """Create a dimension from json.

        Parameters
        ----------
        id : String
            See BaseItem documentation
        index : Integer
            See BaseItem documentation
        json : Dict
            Json part of the dimension, containing category

        Returns
        -------
        Dimension
            Return a dimension object
        """

        label = json.get('label')
        dimension = cls(id, index, label, size)
        category = json.get('category')
        index = category.get('index')
        for index, id in [(k, v) for k, v in sorted(zip(
            map(lambda x: int(x), index.values()),
            index.keys()
        ))]:
            dimension_label = category.get('label').get(id)
            dimension_category = Category(id, index, dimension_label)
            dimension.add_category(dimension_category)
        return dimension
