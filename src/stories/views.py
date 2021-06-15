from django.http.response import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StageListSerializer, StageDetailSerializer
from .models import Stage
from rest_framework import generics
from .permissions import IsAdminUserOrReadOnly


class StageList(generics.ListCreateAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageListSerializer

class StageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]

    queryset = Stage.objects.all()
    serializer_class = StageDetailSerializer

