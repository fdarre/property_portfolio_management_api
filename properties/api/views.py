from rest_framework import viewsets

from ..models import Building
from .serializers import BuildingSerializer


class BuildingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing building instances.
    """
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()