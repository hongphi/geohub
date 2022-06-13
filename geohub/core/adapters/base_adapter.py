"""
This module is responsible for translating the API I/O
"""

from . import AbstractBaseAdapter


class BaseAdapter(AbstractBaseAdapter):
    """Base adapater for api contract"""

    def __init__(self, usecase, schema):
        self.usecase = usecase()
        self.schema = schema

    def __repr__(self):
        return "{}(entity, usecase)".format(self.__class__.__name__)

    def find_all(self):
        data_model = self.usecase.find_all()
        dump = self.schema(many=True).dump(data_model)
        return dump

    def delete(self, obj_id):
        return self.usecase.delete(obj_id)
