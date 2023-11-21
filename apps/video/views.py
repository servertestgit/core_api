from django.shortcuts import render
from rest_framework.response import Response
from .models import VideoApp
from .serializer import VideoAppSerializer
from rest_framework.views import APIView
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404


class VideoAppList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        candidates = VideoApp.objects.all()
        serializer = VideoAppSerializer(candidates, many=True)
        if serializer:
            response_data = {"videos": serializer.data}
            return Response(response_data, status=status.HTTP_200_OK)

        return Response(
            {"error": "No Videos to list"},
            status=status.HTTP_404_NOT_FOUND)


class VideoDetailView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, videoId, format=None):
        try:
            video_id = int(videoId)
        except ValueError:
            return Response(
                {'error': 'Video ID must be an integer'},
                status=status.HTTP_400_BAD_REQUEST)

        video = get_object_or_404(VideoApp, id=video_id)
        serializer = VideoAppSerializer(video)

        return Response({'video': serializer.data}, status=status.HTTP_200_OK)
