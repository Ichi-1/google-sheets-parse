from rest_framework.serializers import ModelSerializer
from .models import Order

class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"


class ChartSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = ("value_usd", "supply_date")


class TotalValueUsdSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = ("value_usd",)