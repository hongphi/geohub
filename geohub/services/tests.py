import pytest
from django.test import TestCase
from django.urls import reverse
import json


@pytest.mark.django_db
def test_view_services(client):
    res = client.get(reverse('api:api-services'))
    assert res.status_code == 200


@pytest.mark.django_db
def test_view_services_search(client, productZ):
    url = reverse('api:api-services') + "?query=ZK"
    res = client.get(url)
    data = json.loads(res.content)
    assert len(data) == 1


@pytest.mark.django_db
def test_view_services_search_order(client, productZ, productM, productA):
    url = reverse('api:api-services') + "?query=ZK&sort_by=name"
    res = client.get(url)
    data = json.loads(res.content)
    count = 1
    for p in data[1:]:
        assert p['name'] >= p[count-1]
        count += 1


@pytest.mark.django_db
def test_service_details(client, productZ):
    res = client.get(reverse("api:service-details", kwargs={'slug': productZ.slug}))
    assert res.status_code == 200
