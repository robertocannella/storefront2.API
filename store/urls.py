from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.product_list, name='products'),
    path('products/<int:product_id>', views.product_detail, name='product-detail'),
    path('collections/', views.collection_list, name='collections'),
    path('collections/<int:pk>', views.collection_detail, name='collection-detail')
]

