from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id", "name", "description", "category", "price", 
            "brand", "quantity", "created_at", "updated_at"
        ]

    # Validation for price (must be positive)
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be a positive value.")
        return value

    # Validation for quantity (must be non-negative)
    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        return value
