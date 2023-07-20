from rest_framework import serializers
from .models import *

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'total', 'collection', 'id', 'attributesName1', 'attributes1',  'attributesName2', 'attributes2',  'attributesName3', 'attributes3',  'attributesName4', 'attributes4',  'attributesName5', 'attributes5',  'attributesName6', 'attributes6',  'attributesName7', 'attributes7',  'attributesName8', 'attributes8' )


class CollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('name', 'id', 'category', 'heading', 'desc', 'description1', 'description2', 'description3', 'description4', 'description5', 'description6' )


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'id']

class FaqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('question','answer')

class TechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ('left_heading', 'left_description', 'left_logo', 'right_heading', 'right_description', 'right_logo')

