from rest_framework import serializers

from building.models import Building


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ("id", "name", "entity", "start_date", "end_date", "created_at", "updated_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")