from abc import ABC

from geohub.core.adapters.base_adapter import BaseAdapter
from geohub.core.usecases.product_usecase import ProductUseCase
from geohub.services.api.serializers import ProductSerializer


class ProductAdapter(BaseAdapter, ABC):
    """Book adapter with crud methods"""

    def __init__(self):
        """Initialize class with book use case and book schema"""
        super().__init__(ProductUseCase, ProductSerializer)

    def __repr__(self):
        """CLass representation"""
        return "{}()".format(self.__class__.__name__)

    def find_all(self):
        return self.usecase.find_all()

    def search_product(self, query):
        return self.usecase.search_product(query)

    def create(self, data):
        if self.schema(data).is_valid():
            self.usecase.create(data)


    def get_product(self, slug):
        return self.usecase.get_product(slug)
