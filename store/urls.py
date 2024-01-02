from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.product_list, name='products'),
    path('products/<int:product_id>', views.product_detail, name='product_detail')
]
