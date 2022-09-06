from django.urls import path
from .views import OrdersViewSet, ChartViewSet

app_name = 'google_sheets'

urlpatterns = [
    path('orders/', OrdersViewSet.as_view({"get": "list"})),
    path('chart/', ChartViewSet.as_view({"get": "list"})),
    path('total-count/', ChartViewSet.as_view(
        {
            "get": "retrieve"
        }
    ))
]