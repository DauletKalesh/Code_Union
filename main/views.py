from rest_framework import generics
from .models import Currency
from .serializers import CurrencySerializer

class CurrencyList(generics.ListAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()

class CurrencyDetail(generics.RetrieveAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()