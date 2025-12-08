from rest_framework import serializers

from building.models import Building, Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ("id", "name", "employees_count", "external_id")


class BuildingSerializer(serializers.ModelSerializer):

    organizations = OrganizationSerializer(many=True) # nested organizations

    class Meta:
        model = Building
        fields = ("id", "name", "entity", "start_date", "end_date", "created_at", "updated_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")