from rest_framework import serializers
from .models import Person

class PeopleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__' # for all fields
        # fields = ['name', 'age'] # for only given fields
        # exclude = ['id'] # for excluding fields