from rest_framework import serializers
from .models import database

class serialize(serializers.ModelSerializer):
    class Meta:
        model=database
        fields=['id','name','url','uploaded_At']