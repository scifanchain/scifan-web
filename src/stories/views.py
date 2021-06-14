from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StageListSerializer
from .models import Stage


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        stages = Stage.objects.all()
        serializer = StageListSerializer(stages, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StageListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
