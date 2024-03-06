from rest_framework import serializers
from products.models import Category


class CreateCategorySerializer(serializers.Serializer):
    title = serializers.CharField()
    featured_image = serializers.ImageField()


class FetchCategoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'