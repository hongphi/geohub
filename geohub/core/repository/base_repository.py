"""
This Module Provides Basic Repository Functionality
"""
from . import AbstractBaseRepository


class BaseRepository(AbstractBaseRepository):
    """
    Base Repository Class with Basic methods which Product repository will inherit from.
    """

    def __init__(self, entity):
        self.__entity = entity

    def __repr__(self):
        "{}(entity)".format(self.__class__.__name__)

    def __getitem__(self, item):
        return self.__entity.query.get(item)

    def find_by_id(self, object_id):
        return self.__getitem__(object_id)

    def find_all(self):
        return []

    def create(self, data):
        committed = True
        return committed

    def update_or_patch(self, old_data_model, new_data_model):
        committed = True
        return committed

    def delete(self, object_id):
        committed = True
        return committed
