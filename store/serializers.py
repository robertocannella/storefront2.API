from decimal import Decimal, ROUND_HALF_UP
from .models import Collection
from rest_framework import serializers
from store.models import Product


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title','featured_product','products_count']

    products_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','slug','inventory','price','price_with_tax','collection']
    price = serializers.DecimalField(max_digits=10, decimal_places=2,source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # collection = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all)
    # collection = serializers.StringRelatedField()
    # collection = CollectionSerializer()
    # collection = serializers.HyperlinkedRelatedField(
    #         queryset=Collection.objects.all(),
    #         view_name='collection-detail'
    # )

    def calculate_tax(self, product):
        tax_rate = Decimal('1.1')  # Using a string to initialize ensures precision
        calculated_tax = product.unit_price * tax_rate
        # Round to 3 decimal places
        return calculated_tax.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)


