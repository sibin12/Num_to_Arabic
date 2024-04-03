from rest_framework import serializers

class NumberSerializer(serializers.Serializer):
    number = serializers.DecimalField(max_digits=10, decimal_places=2)  # Adjust max_digits and decimal_places as needed
