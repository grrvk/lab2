from rest_framework import serializers

from .models import Transport


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = [
            'route',
            'type',
            'number',
            'num_of_passengers',
        ]