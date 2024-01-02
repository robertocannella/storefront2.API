from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer


# PRODUCTS
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('ok')




@api_view(['GET'])
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


# COLLECTIONS
@api_view(['GET'])
def collection_list(request):
    collections = Collection.objects.all()
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data,status=200)


@api_view(['GET'])
def collection_detail(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)