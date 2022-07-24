"""
3.10.1 View はクライアント（ブラウザなど）からのリクエストに応じ、
どういった処理をするか（どの API を提供するか）を司っています。
"""
from django.shortcuts import render

from rest_framework import generics

from user.serializers import UserSerializer

# トークンの発行を実装
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerializer, AuthTokenSerializer 

# ユーザー情報の更新
from rest_framework import generics, authentication, permissions  


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    # 3.10.2 serializer_class に作った UserSerializer を指定しています。
    serializer_class = UserSerializer

# 4.2.1 トークンの発行を実装
class CreateTokenView(ObtainAuthToken):
    """4.2.3 Create a new auth token for user, restrict who can see Todo"""
    serializer_class = AuthTokenSerializer
    """4.2.3 renderer_classes = ブラウザ上で発行されたトークンを確認することができます"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

# ユーザー情報の更新
class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    # authentication, permissions = 認証と許可
    # トークン認証を利用し、認証されたユーザーのみ閲覧・編集を許可する    
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    # 認証されていないユーザーは閲覧のみ許可、といった制限もできます

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user