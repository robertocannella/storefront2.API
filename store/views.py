from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def product_list(request):
    return Response("Hello World")


@api_view(['GET'])
def product_detail(request, product_id):
    return Response(product_id)