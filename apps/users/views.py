from rest_framework import status, viewsets
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from apps.general.authentication import get_user_auth_data
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from apps.users.forms import SignUpForm
from apps.users.models import User, Code
from apps.users.serializers import CodeSerializer, UserAvatarSerializer
import random


@api_view(['POST'])
def signup(request):
    data = request.data
    form = SignUpForm({
        'username': data.get('username'),
        'first_name': data.get('first_name'),
        'last_name': data.get('last_name'),
        'password1': data.get('password'),
        'password2': data.get('password')
    })

    if form.is_valid():
        user = form.save()
        user.pass_word = data.get('password')
        user.save()
        code_default = random.randint(10000, 99999)
        code = Code.objects.create(user=user, code=code_default)
        serializer = CodeSerializer(code)
        return Response(serializer.data['code'], status=status.HTTP_201_CREATED)
    else:
        usr = User.objects.get(username=data.get('username'))
        code_ = Code.objects.get(user=usr)
        code_default = random.randint(10000, 99999)
        code_.code = code_default
        code_.save()
        serializer = CodeSerializer(code_)
        return Response(serializer.data['code'], status=status.HTTP_200_OK)


@api_view(['POST'])
@parser_classes([FormParser, MultiPartParser])
def user_avatar_update(request):
    data = request.data
    try:
        user = User.objects.get(username=data.get('username'))
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

    serializer = UserAvatarSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
