from django.urls import path
from rest_framework.routers import DefaultRouter

from store.apps import StoreConfig
from store.views import (NetworkCreateAPIView, NetworkDestroyAPIView,
                         NetworkListAPIView, NetworkRetrieveAPIView,
                         NetworkUpdateAPIView, ProductViewSet)

app_name = StoreConfig.name

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")

urlpatterns = [
    path("network/create/", NetworkCreateAPIView.as_view(), name="network-create"),
    path("network/", NetworkListAPIView.as_view(), name="network-list"),
    path(
        "network/update/<int:pk>/",
        NetworkUpdateAPIView.as_view(),
        name="network-update",
    ),
    path(
        "network/delete/<int:pk>/",
        NetworkDestroyAPIView.as_view(),
        name="network-delete",
    ),
    path(
        "network/<int:pk>/", NetworkRetrieveAPIView.as_view(), name="network-retrieve"
    ),
] + router.urls
