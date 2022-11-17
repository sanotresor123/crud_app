from rest_framework import serializers
from.models import *

class AppSerializers (serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id', 'firstName', 'lastName', 'email', 'phoneNumber', 'age']