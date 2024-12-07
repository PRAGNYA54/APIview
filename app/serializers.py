from rest_framework import serializers
from app.models import *
class Empmodel(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields='__all__'