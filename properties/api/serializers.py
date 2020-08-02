from rest_framework import serializers
from ..models import Building

# Serializers define the API representation.
class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'
