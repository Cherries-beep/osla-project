from django.urls import path
from rest_framework.routers import DefaultRouter

from building.api.views import BuildingViewSet, OrganizationViewSet

router = DefaultRouter()
router.register(r"buildings", BuildingViewSet, basename="building")
router.register(r"organizations", OrganizationViewSet, basename="organization")

urlpatterns = router.urls