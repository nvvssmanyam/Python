from rest_framework import serializers
from .models import Location, Department, Category, SubCategory

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ['pk']

    def validate_location(self, value):
        qs = Location.objects.filter(locName_iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exist() :
            raise serializers.ValidationError("The location already exist")
        return value

    def update(self, Location, validated_data):
        Location.locName = validated_data.get('locName', Location.locName)
        Location.save()
        return Location

class LocationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ('locName')

    def create(self, validated_data):
        locName = validated_data.pop('locName')
        location = Location.objects.create(**validated_data)

        return location

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = '__all__'
