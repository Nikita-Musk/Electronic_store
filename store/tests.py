from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Network, Product
from users.models import User


class NetworkTestCase(APITestCase):
    """Тесты для проверки функционала связанного с сетями."""

    def setUp(self):
        """Подготовка тестовых данных перед каждым тестом."""

        self.user = User.objects.create(email="test@testov.com", password="test")
        self.client.force_authenticate(user=self.user)
        self.network = Network.objects.create(
            name="Сеть 1",
            email="network1@gmail.com",
            country="Страна 1",
            city="Город 1",
            street="Улица 1",
            house_number=1,
            level=0,
            debt="0.00",
        )

    def test_network_list(self):
        """Тестирование списка сетей."""

        url = reverse("store:network-list")
        data = [
            {
                "id": self.network.pk,
                "name": self.network.name,
                "email": self.network.email,
                "country": self.network.country,
                "city": self.network.city,
                "street": self.network.street,
                "house_number": self.network.house_number,
                "level": self.network.level,
                "debt": self.network.debt,
                "supplier": None,
            }
        ]
        response = self.client.get(url)
        result = response.json()
        for item in data:
            item.pop("created_at", None)
        for item in result:
            item.pop("created_at", None)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_network_retrieve(self):
        """Тестирование получения данных сети по pk."""

        url = reverse("store:network-retrieve", args=(self.network.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.network.name)

    def test_network_create(self):
        """Тестирование создания сети."""

        url = reverse("store:network-create")
        data = {
            "name": "ИП",
            "email": "network2@gmail.com",
            "country": "Страна 2",
            "city": "Город 2",
            "street": "Улица 2",
            "house_number": 2,
            "level": 2,
            "debt": 0.01,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Network.objects.all().count(), 2)

    def test_network_update(self):
        """Тестирование обновления существующей сети."""

        url = reverse("store:network-update", args=(self.network.pk,))
        data = {"name": "ИП 1"}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), "ИП 1")

    def test_network_delete(self):
        """Тестирование удаления сети."""

        url = reverse("store:network-delete", args=(self.network.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Network.objects.all().count(), 0)


class ProductTestCase(APITestCase):
    """Тесты для проверки функционала связанного с продуктами."""

    def setUp(self):
        """Подготовка тестовых данных перед каждым тестом."""

        self.user = User.objects.create(email="test2@testov.com", password="test")
        self.client.force_authenticate(user=self.user)
        self.network = Network.objects.create(
            name="Сеть 1",
            email="network1@gmail.com",
            country="Страна 1",
            city="Город 1",
            street="Улица 1",
            house_number=1,
            level=0,
            debt=0.00,
        )
        self.product = Product.objects.create(
            name="Продукт 1",
            model="Модель 1",
            launch_date="2020-01-01",
            supplier=self.network,
        )

    def test_product_list(self):
        """Тестирование списка продуктов."""

        url = reverse("store:products-list")
        data = [
            {
                "id": self.product.pk,
                "name": self.product.name,
                "model": self.product.model,
                "launch_date": self.product.launch_date,
                "supplier": self.network.pk,
            }
        ]
        response = self.client.get(url)
        result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, data)

    def test_product_retrieve(self):
        """Тестирование получения данных продукта по pk."""

        url = reverse("store:products-detail", args=(self.product.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.product.name)

    def test_product_create(self):
        """Тестирование создания продукта."""

        url = reverse("store:products-list")
        data = {
            "name": "Продукт 2",
            "model": "Модель 2",
            "launch_date": "2022-01-01",
            "supplier": self.network.pk,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.all().count(), 2)

    def test_product_update(self):
        """Тестирование обновления существующего продукта."""

        url = reverse("store:products-detail", args=(self.product.pk,))
        data = {"name": "Продукт 3"}
        response = self.client.patch(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Продукт 3")

    def test_product_delete(self):
        """Тестирование удаления продукта."""

        url = reverse("store:products-detail", args=(self.product.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.all().count(), 0)
