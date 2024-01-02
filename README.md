# Setup

* Update DATABASE variables in /storefront/settings.py


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

