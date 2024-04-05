from rest_framework import serializers
from .models import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
    
        def create(self, validated_data):
            company = Company.objects.create(name=validated_data['name'], description=validated_data['description'], city=validated_data['city'])
            return company
        
        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('description', instance.description)
            instance.city = validated_data.get('city', instance.city)
            instance.save()
            return instance
    
class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'
    
        def create(self, validated_data):
            return Vacancy.objects.create(name=validated_data['name'], description=validated_data['description'], salary=validated_data['salary'], company=validated_data['company'])
        
        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.description = validated_data.get('description', instance.description)
            instance.salary = validated_data.get('salary', instance.salary)
            instance.company = validated_data.get('company', instance.company)
            instance.save()
            return instance
