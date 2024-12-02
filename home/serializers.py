from rest_framework import serializers
from .models import Person,Color
import re as regex


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['color_name', 'id']


class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    color_info = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__' # for all fields
        # depth = 1
        # fields = ['name', 'age'] # for only given fields
        # exclude = ['id'] # for excluding fields

    def get_color_info(self, data):
        color_obj = Color.objects.get(id= data.color.id)

        return {"color_name": color_obj.color_name, "hex_code": '#000'}

    def validate(self, data):
        unique_regex =  '^[a-zA-Z\s]+$'
        print(data['name'])
        if not regex.match(unique_regex, data['name']):
            raise serializers.ValidationError('Name should contain only letters and spaces')


        if data['age'] < 18:
            raise serializers.ValidationError('Age should be greater then 18')
        return data