from django.db.models import fields
from django.http import request
from rest_framework import serializers
from .models import Stage


class StageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = [
            'id',
            'title',
            'created_time',
            'maturity',
            'version',
            'content',
            'authors',
            'owner',
        ]

    # def create(self, validated_data):
    #     validated_data.authors.set(1,)
    #     # authors_data = validated_data.pop('authors')
    #     instance = Stage.objects.create(**validated_data)
    #     # instance.authors.add(request.user.id)

    #     return instance

class StageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'
        # exclude = ['owner']
