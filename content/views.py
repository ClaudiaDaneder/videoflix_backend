from django import views
from django.conf import settings
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from content.models import CATEGORIES, Video
from content.serializers import VideoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHETTL', DEFAULT_TIMEOUT)

class VideoViewSet(viewsets.ViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    """
    A simple ViewSet for listing or retrieving users.
    """
    @cache_page(CACHE_TTL)
    def list(self, request):
        queryset = Video.objects.all()
        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoriesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = [
            {
                'value': key,
                'name': name
            } for key, name in CATEGORIES
        ]
        return Response(categories)