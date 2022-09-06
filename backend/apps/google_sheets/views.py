from .models import Order
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response
from .serializers import OrderSerializer, ChartSerializer, TotalValueUsdSerializer
from django.db.models import Sum

class OrdersViewSet(ModelViewSet):
    """
    Return List of current orders data
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]


class ChartViewSet(ModelViewSet):
    """
    Return data relevant for chart
    """
    queryset = Order.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return ChartSerializer
        if self.action == 'retrieve':
            return TotalValueUsdSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Return aggregated total value in USD
        """
        qs = self.queryset.aggregate(Sum('value_usd'))
        return response.Response(qs)
