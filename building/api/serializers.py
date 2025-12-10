from rest_framework import serializers

from building.models import Building, Organization


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ("id", "name", "employees_count", "external_id")


class BuildingSerializer(serializers.ModelSerializer):

    organizations = OrganizationSerializer(many=True, read_only=True)
    organization_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Organization.objects.all(),
        source="organizations"
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
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")