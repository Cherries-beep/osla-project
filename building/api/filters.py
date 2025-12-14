import django_filters

from building.models import Building, Organization


class BuildingFilter(django_filters.FilterSet):
    """Фильтр для объектов строительства.

    Args:
        exact_organizations: Фильтр по точному совпадению всех организаций
        organizations: Фильтр по наличию хотя бы одной организации
    """

    exact_organizations = django_filters.ModelMultipleChoiceFilter(  # Для точного совпадения (только указанные организации)
        field_name="organizations", 
        queryset=Organization.objects.all(), 
        conjoined=True
    )

    organizations = django_filters.ModelMultipleChoiceFilter(  # Для фильтрации по наличию любой из указанных
        field_name="organizations", 
        queryset=Organization.objects.all()
    )

    class Meta:
        model = Building
        fields = ["name", "entity"]