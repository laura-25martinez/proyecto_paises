from rest_framework import viewsets, permissions
from .models import Country, Department, City
from .serializer import CountrySerializer, DepartmentSerializer, CitySerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions_classes = [permissions.AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions_classes = [permissions.AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]

class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions_classes = [permissions.AllowAny]
        else:
            permissions_classes = [IsAuthenticated]
        return [permissions() for permissions in permissions_classes]