from rest_framework import serializers
from .models import AcademicLevel, TypeActivity


class AcademicLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicLevel
        fields = '__all__'


class TypeActivitySerializer(serializers.ModelSerializer):    
    class Meta:
        model = TypeActivity
        fields = '__all__'
        
