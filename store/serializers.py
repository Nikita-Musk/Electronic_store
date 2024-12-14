from rest_framework import serializers

from store.models import Network, Product


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = "__all__"


class NetworkUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        exclude = ("debt",)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
