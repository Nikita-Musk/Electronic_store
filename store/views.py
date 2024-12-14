from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from store.models import Network, Product
from store.permissions import IsActive
from store.serializers import (NetworkSerializer, NetworkUpdateSerializer,
                               ProductSerializer)


class ProductViewSet(viewsets.ModelViewSet):
    """Контроллер предоставляет действия CRUD для продуктов."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive]


class NetworkCreateAPIView(CreateAPIView):
    """Контроллер для создания новых объектов сети."""

    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActive]


class NetworkListAPIView(ListAPIView):
    """Контроллер для отображения списка всех сетей."""

    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("country",)


class NetworkRetrieveAPIView(RetrieveAPIView):
    """Контроллер для отображения деталей конкретной сети."""

    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActive]


class NetworkUpdateAPIView(UpdateAPIView):
    """Контроллер для обновления существующей сети."""

    queryset = Network.objects.all()
    serializer_class = NetworkUpdateSerializer
    permission_classes = [IsActive]


class NetworkDestroyAPIView(DestroyAPIView):
    """Контроллер для удаления сети."""

    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActive]
