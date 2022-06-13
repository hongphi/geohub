"""
This Module Provides advanced repository functionalities for Book Objects
"""

from .base_repository import BaseRepository
from ..entities.product_entity import ProductEntity
from ...services.models import Product
from django.db.models import Q
from django.shortcuts import get_object_or_404


class ProductRepository(BaseRepository):
    """Product repository access"""

    def __init__(self):
        """Initialize values self.class"""
        super().__init__(ProductEntity)

    def __repr__(self):
        """Representation of class"""
        return "{}()".format(self.__class__.__name__)

    def search_product(self, query):
        return Product.objects.filter(Q(name__icontains=query) |
                                      Q(os__icontains=query))

    def get_product(self, slug):
        return get_object_or_404(Product, slug=slug)

    def find_all(self):
        return Product.objects.all()

    @classmethod
    def find_by_name(cls, name):
        """Get product by title if exists"""
        return Product.objects.filter(name__iexact=name).first()

    def create(self, data):
        p = Product(**data)
        p.save()
        return p

    def update_or_patch(self, old_data_model, new_data_model):
        for field in new_data_model:
            old_data_model[field] = new_data_model[field]
        old_data_model.save()

    def delete(self, object_id):
        Product.objects.filter(id=object_id).delete()
