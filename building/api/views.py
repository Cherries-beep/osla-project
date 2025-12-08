from rest_framework.viewsets import ModelViewSet
from building.api.serializers import BuildingSerializer, OrganizationSerializer
from building.models import Building, Organization


class BuildingViewSet(ModelViewSet):
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()


class OrganizationViewSet(ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
