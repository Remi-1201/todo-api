
"""
3.9.1 serializers = クエリセットやモデルのインスタンスのような
複雑なデータをJSON、XMLなどの出力可能なデータに書き出すこと。
"""
from django.contrib.auth import get_user_model

from rest_framework import serializers

from django.contrib.auth import get_user_model, authenticate  # 4.1 トークンの発行を実装


class UserSerializer(serializers.ModelSerializer):
    """
    3.9.2 ModelSerializer = Django のモデルと紐づいています。
    モデルに基づいてフィールドとバリデータが自動的に Serializer にも適用されます
    """

    class Meta:
        # 3.9.3 get_user_model 関数は、そのプロジェクトで使用している User モデルを取得します。 
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        user = get_user_model().objects.create_user(**validated_data)

        return user

    # 5.1 認証されたユーザーが自身の登録情報を更新できるようにします
    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        # 5.1.1 .pop('password') = 更新前のパスワードを削除
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

# 4. トークン認証 
"""
作成したユーザーがパスワードを変更したいとなった時、
認証されたユーザー（本人）だけが変更できるように制御
"""
class AuthTokenSerializer(serializers.Serializer):
    """
    4.1.1 必要なユーザー情報の項目（メールアドレスとパスワード）を設定
    """
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """4.1.2 必要なユーザー情報の項目をvalidate 関数で検証"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        # 入力された情報が一致しなかった場合にエラーメッセージを表示する
        if not user:
            msg = ('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs