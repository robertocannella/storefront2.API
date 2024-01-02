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