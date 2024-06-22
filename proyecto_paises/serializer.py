from rest_framework import serializers
from .models import Country, Department, City
from django.conf import settings

class CountrySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required=False)
    class Meta:
        model = Country
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        country = super().create(validated_data)
        if image:
            country.image_url = self.save_image(country, image)
            country.save()
        return country

    def save_image(self, country, image):
        from django.core.files.storage import default_storage
        from django.core.files.base import ContentFile
        import os

        path = default_storage.save(os.path.join('images', str(country.id) + '_' + image.name), ContentFile(image.read()))
        return settings.MEDIA_URL + path

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'