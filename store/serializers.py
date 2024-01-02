from decimal import Decimal, ROUND_HALF_UP

from rest_framework import serializers

from store.models import Product


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2,source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product):
        tax_rate = Decimal('1.1')  # Using a string to initialize ensures precision
        calculated_tax = product.unit_price * tax_rate
        # Round to 3 decimal places
        return calculated_tax.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)


