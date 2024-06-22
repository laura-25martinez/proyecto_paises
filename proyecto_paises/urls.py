from django.urls import include, path
from rest_framework import routers
from .views import CountryViewSet, DepartmentViewSet, CityViewSet

router = routers.DefaultRouter()
router.register(r'country', CountryViewSet)
router.register(r'department', DepartmentViewSet)
router.register(r'city', CityViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls))
]
