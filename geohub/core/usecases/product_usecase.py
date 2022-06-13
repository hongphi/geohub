"""This Module contains the Usecases - write business codes rules"""

from . import AbstractBaseBookUseCase
from ..repository.product_repository import ProductRepository


class ProductUseCase(AbstractBaseBookUseCase):
    """"This Class contains the App Usecases"""

    def __init__(self):
        """Init class values"""
        self.repository = ProductRepository()

    def __repr__(self):
        """Representation of class"""
        return "{}()".format(self.__class__.__name__)

    def search_product(self, query):
        return self.repository.search_product(query)

    def get_product(self, slug):
        return self.repository.get_product(slug)

    def find_all(self):
        """Find all books"""
        return self.repository.find_all()

    def find_by_title(self, title):
        """Find product by tilte"""
        return self.repository.find_by_name(title)

    def create(self, data):
        """Create book if it doesn't exists"""
        found = self.repository.find_by_title(data.title)
        if not found:
            return self.repository.create(data)
        return False

    def update_or_patch(self, product_id, data):
        """Update book if exists"""
        found = self.repository.find_by_id(product_id)
        if found:
            return self.repository.update_or_patch(found, data)
        return False

    def delete(self, product_id):
        """Delete book if exists"""
        return self.repository.delete(product_id)
