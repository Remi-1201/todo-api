# 6.6 Todo app の作成 / Serializer の作成
from rest_framework import serializers

from core.models import Todo
from user.serializers import UserSerializer

class TodoSerializer(serializers.ModelSerializer):
    """Serializer for Todo objects"""

    user = UserSerializer(read_only=True)
    """6.6.1 Todo モデルと紐づいている User モデルの user フィールドに関しては 
    UserSerializer でシリアライズします。"""

    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'content', 'created_at', 'is_completed')
        read_only_fields = ('id', 'user',)