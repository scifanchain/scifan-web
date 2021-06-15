from django.db.models import fields
from rest_framework import serializers
from .models import Stage
from django.contrib.auth.models import User


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
            'owner',
        ]

    # def create(self, validated_data):
    #     # validated_data.authors.set(request.user)
    #     # authors_data = validated_data.pop('authors')
    #     instance = Stage.objects.create(**validated_data)
    #     user_id = User.objects.get(pk=2)
    #     instance.authors.add(user_id.id,)

    #     return instance

    # user = User.objects.only('id').get(id=data['user_id'])
    # obj = ModelA.objects.create(phone=data['phone'], user=user)

class StageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'
        # exclude = ['owner']
