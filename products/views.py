from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['name', 'description', 'category']
    filter_fields = ['category']
    ordering_fields = ['name', 'price']

    def get_queryset(self):
        queryset = Product.objects.all()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(name__icontains=search_query) | queryset.filter(
                description__icontains=search_query)

        return queryset
