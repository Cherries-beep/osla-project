from rest_framework.viewsets import ModelViewSet

from building.api.serializers import BuildingSerializer
from building.models import Building


class BuildingViewSet(ModelViewSet):
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()

