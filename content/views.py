from django import views
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from content.models import CATEGORIES, Video
from content.serializers import VideoSerializer

class VideoViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Video.objects.all()
        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoriesView(APIView):

    def get(self, request):
        categories = [
            {
                'value': key,
                'name': name
            } for key, name in CATEGORIES
        ]
        return Response(categories)