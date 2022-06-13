import pytest

from geohub.services.models import Product
from geohub.users.models import User
from geohub.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.mark.django_db
@pytest.fixture
def productZ():
    p = Product(name="ZK service", price=100, os="Apple")
    p.save()
    return p


@pytest.mark.django_db
@pytest.fixture
def productM():
    p = Product(name="MQ service", price=100, os="Apple")
    p.save()
    return p


@pytest.mark.django_db
@pytest.fixture
def productA():
    p = Product(name="AS service", price=100, os="Apple")
    p.save()
    return p
