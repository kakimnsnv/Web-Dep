from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

        def create(self, validated_data):
            return Product.objects.create(name=validated_data['name'], description=validated_data['description'], likes=validated_data['likes'], price=validated_data['price'], count=validated_data['count'], is_active=validated_data['is_active'], rating=validated_data['rating'], category=validated_data['category'])
        
        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('description', instance.description)
            instance.likes = validated_data.get('likes', instance.likes)
            instance.price = validated_data.get('price', instance.price)
            instance.count = validated_data.get('count', instance.count)
            instance.is_active = validated_data.get('is_active', instance.is_active)
            instance.rating = validated_data.get('rating', instance.rating)
            instance.category = validated_data.get('category', instance.category)
            instance.save()
            return instance

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

        def create(self, validated_data):
            return Category.objects.create(name=validated_data['name'], description=validated_data['description'], likes=validated_data['likes'])
        
        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('description', instance.description)
            instance.likes = validated_data.get('likes', instance.likes)
            instance.save()
            return instance