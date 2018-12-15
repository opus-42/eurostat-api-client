from src.utils.property_decorators import property_is_int, property_is_string


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

    def __init__(self, id, index, label):
        super().__init__(id, index, label)
        self.categories = []

    @property
    def category_counts(self):
        return len(self.categories)

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
        self.categories.append(category)
