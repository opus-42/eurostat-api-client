from src.utils.property_decorators import property_is_int, property_is_string


class Category(object):

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
