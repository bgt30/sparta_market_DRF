from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_size_query_param = 'page_size'

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.select_related('author').prefetch_related('tags')
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'author']
    search_fields = ['title', 'content', 'author__username']
    ordering_fields = ['created_at', 'likes']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Product.objects.filter(author=self.request.user)

class ProductLikeView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if request.user in product.likes.all():
            product.likes.remove(request.user)
            return Response({"message": "좋아요 취소"})
        else:
            product.likes.add(request.user)
            return Response({"message": "좋아요 추가"}) 