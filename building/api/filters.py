
import django_filters
from building.models import Building, Organization


class BuildingFilter(django_filters.FilterSet):
    
    exact_organizations = django_filters.ModelMultipleChoiceFilter( # Для точного совпадения (только указанные организации)
        field_name='organizations',
        queryset=Organization.objects.all(),
        conjoined=True 
    )
    
    organizations = django_filters.ModelMultipleChoiceFilter( # Для фильтрации по наличию любой из указанных 
        field_name='organizations',
        queryset=Organization.objects.all()
    )
    
    class Meta:
        model = Building
        fields = ['name', 'entity']