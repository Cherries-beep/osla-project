from django.urls import path
from building.api.views import BuildingViewSet

building = BuildingViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
building_detail = BuildingViewSet.as_view({
    'get': 'retrieve',
})


urlpatterns = [
    path('', building, name='building_list'),
    path('<int:pk>/', building_detail, name='building_detail')
]