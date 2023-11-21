from rest_framework import serializers
from .models import VideoApp, ModulClass, Comment
from apps.users.serializers import UserReadSerializer


class ModulSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModulClass
        fields = ('id', 'name', 'all_videos',)


class CommentSerializer(serializers.ModelSerializer):
    created_by = UserReadSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'created_by', 'comment',)


class VideoAppSerializer(serializers.ModelSerializer):
    modul = ModulSerializer(read_only=True)
    comment = CommentSerializer()

    class Meta:
        model = VideoApp
        fields = ('id', 'modul', 'name',
                  'description', 'comment', 'get_thumbnail',)
