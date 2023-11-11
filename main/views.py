from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Currency
from .serializers import CurrencySerializer

class CurrencyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'per_page'
    max_page_size = 100

class CurrencyList(generics.ListAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
    pagination_class = CurrencyPagination
    permission_classes = (permissions.IsAuthenticated,)

class CurrencyDetail(generics.RetrieveAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
    permission_classes = (permissions.IsAuthenticated,)