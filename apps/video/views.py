from django.shortcuts import render
from requests import Response
from .models import VideoApp
from .serializer import VideoAppSerializer
from rest_framework.views import APIView
from rest_framework import status, permissions

class VideoAppList(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, format=None):
        candidates = VideoApp.objects.all()
        serializer = VideoAppSerializer(candidates, many=True)
        if serializer:
            return Response(
                {"videos": serializer.data},
                status=status.HTTP_200_OK)

        return Response(
            {"error": "No Videos to list"},
            status=status.HTTP_404_NOT_FOUND)


class VideoDetailView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, videoId, format=None):
        try:
            video_id = int(videoId)
        except:
            return Response(
                {'error': 'Video ID must be an integer'},
                status=status.HTTP_404_NOT_FOUND)

        if VideoApp.objects.filter(id=video_id).exists():
            video = VideoApp.objects.get(id=video_id)

            serializer = VideoAppSerializer(video)

            return Response({'video': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'Video with this ID does not exist'},
                status=status.HTTP_404_NOT_FOUND)