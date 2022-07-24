# 3.3 User モデルの作成
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings    # あとで使います。

# 3.3.1 BaseUserManager=マネージャーをカスタマイズする際に継承
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

# 3.3.1 AbstractBaseUser -> 動作を柔軟に定義したい際に利用
# - パーミッションの機能を利用したい場合は、
# - PermissionMixin を同時に継承しておく
class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'    # 3.3 デフォルトは名前入力、今回はメールアドレスにカスタム

# 6.1 Todo モデルの作成 / 最下部に追加
class Todo(models.Model):
    """Todo object"""
    user = models.ForeignKey(
        # 6.1.1 settings.AUTH_USER_MODEL= Userモデルをカスタマイズしたので、
        # - Userモデルを参照するよう指定 ↓
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )

    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title