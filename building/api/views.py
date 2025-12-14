from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from building.api.filters import BuildingFilter
from building.api.serializers import BuildingSerializer, OrganizationSerializer
from building.models import Building, Organization


class BuildingViewSet(ModelViewSet):
    """ViewSet для CRUD и управления связью с организациями"""

    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BuildingFilter

    @action(
        detail=True, methods=["get"], url_path="organizations"
    )  # GET /building/buildings/1/organizations/
    def get_organizations(self, request, pk=None):
        """Получить список организаций конкретного объекта

        Args:
            request: запрос
            pk: ID объекта строительства

        Returns:
            Response: Сериализованный список организаций
        """
        building = self.get_object()
        organizations = building.organizations.all()
        serializer = OrganizationSerializer(organizations, many=True)

        return Response(serializer.data)
    
    @action(detail=True, methods=['post', 'delete'], url_path='organizations/(?P<organization_id>\d+)')
    def manage_organization(self, request, pk=None, organization_id=None):  # POST и DELETE /building/buildings/1/organizations/3/
        """Добавить или удалить связь здания с организацией.

        Args:
            request: запрос
            pk: ID объекта строительства
            organization_id: ID организации для связи

        Returns:
            Response: Статус выполнения операции
        """
        building = self.get_object()

        try:
            organization = Organization.objects.get(id=organization_id)

        except Organization.DoesNotExist:

            return Response(
                {"error": "Организация не найдена"}, status=status.HTTP_404_NOT_FOUND
            )

        if request.method == "POST":
            building.organizations.add(organization)

            return Response(
                {"status": f"Организация {organization.name} добавлена к объекту"},
                status=status.HTTP_200_OK,
            )

        elif request.method == "DELETE":
            building.organizations.remove(organization)

            return Response(
                {"status": f"Организация {organization.name} удалена из объекта"},
                status=status.HTTP_200_OK,
            )


class OrganizationViewSet(ModelViewSet):
    """ViewSet для CRUD организаций.

    Args:
        queryset: Все объекты Organization
        serializer_class: OrganizationSerializer
        filter_backends: Список фильтров
        filterset_fields: Поля для фильтрации
    """
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "external_id", "employees_count"]