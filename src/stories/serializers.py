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
        ]
