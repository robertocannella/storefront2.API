# Setup

* Update DATABASE variables in `/storefront/settings.py`


* From project root, run 

    ```pipenv install```


* Enter virtual environment

    ```pipenv shell```


* Run Migrations

    ```python manage.py migrate```


* Run seed.sql script to populate database


* Create Super User for admin

    ``` python manage.py createsuperuser```


* Install Django REST Framework

  ```pipenv install djangorestframework```

# Create Endpoint

* Create a view in `/store/views.py`
* Include rest_framework imports
```
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def product_list(request):
    return Response("Hello World")
    
   
  ```

* Add URLs file: `/store/urls.py`

  ```
  from django.urls import path
  from . import views
  
  # URLConf
  urlpatterns = [
      path('products/', views.product_list, name='products')
  ]
  
  ```
  
* Add `store/` Endpoint to main URLs file

  ```
  admin.site.site_header = 'Storefront Admin'
  admin.site.index_title = 'Admin'
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('playground/', include('playground.urls')),
      path('store/', include('store.urls')),
      path('__debug__/', include(debug_toolbar.urls)),
  ]
  
  ```
    
* Add Serializers File: `/store/serializers.py`
  
  ``` 
  from rest_framework import serializers
  
  
  class ProductSerializer(serializers.ModelSerializer):
      id = serializers.IntegerField()
      title = serializers.CharField(max_length=255)
      unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
  ```

* Import models and serializers into `/store/views.py`
* Serialize the product and return it in the repsonse

  ``` 
  ... other imports
  
    from .models import Product
    from .serializers import ProductSerializer
  
  ... other functions
    
    @api_view(['GET'])
    def product_detail(request, product_id):
        product=Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
  ```

# Update Settings

* change default decimal behavior in `/storefront/settings.py`

  ``` 
  ... other settings
   
  REST_FRAMEWORK = {
      'COERCE_DECIMAL_TO_STRING': False
  }
  ```

* Set 404 for not found in `/store/views.py`

  ``` 
  ... other imports
  
  from django.shortcuts import get_object_or_404
  
  ... other functions
  
  @api_view(['GET'])
  def product_detail(request, product_id):
      product = get_object_or_404(Product, pk=product_id)
      serializer = ProductSerializer(product)
      return Response(serializer.data)
  ```
  
