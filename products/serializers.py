from rest_framework import serializers
from .models import Product, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['image']

class ProductSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'photos']

    def get_photos(self, obj):
        request = self.context.get('request')
        city_id = request.headers.get('City-ID')
        if city_id:
            photos = obj.photos.filter(city_id=city_id)
        else:
            photos = obj.photos.filter(city__isnull=True)
        return PhotoSerializer(photos, many=True).data
