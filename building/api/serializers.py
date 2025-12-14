from rest_framework import serializers

from building.models import Building, Organization


class OrganizationSerializer(serializers.ModelSerializer):
    """Сериализатор организации"""

    class Meta:
        model = Organization
        fields = (
            "id",
            "name",
            "employees_count",
            "external_id",
            "created_at",
            "updated_at",
        )


class BuildingSerializer(serializers.ModelSerializer):
    """Сериализатор объекта строительства с nested организациями.

    Args:
        organizations : Вложенные организации для GET-запроса
        organization_ids: Список ID организаций для POST/PUT/PATCH

    """

    organizations = OrganizationSerializer(  # только для GET
        many=True, 
        read_only=True
    ) 
    organization_ids = serializers.PrimaryKeyRelatedField(  # (POST/PUT/PATCH). для создания с организациями
        many=True,
        write_only=True,
        queryset=Organization.objects.all(),
        source="organizations",
    )

    class Meta:
        model = Building
        fields = (
            "id",
            "name",
            "entity",
            "start_date",
            "end_date",
            "organizations",
            "organization_ids",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")