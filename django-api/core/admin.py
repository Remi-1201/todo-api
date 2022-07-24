# 3.8 管理画面にモデルを登録
# - 作成した User モデルを管理画面で確認できるよう、admin.py に変更を加えます
from django.contrib import admin
"""
BaseUserAdmin = デフォルトの UserAdmin を BaseUserAdmin としてインポートし、
それを継承することでカスタマイズします
"""
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
"""
gettext as _ = gettext は多言語対応のために利用されます。
慣習的に as _ としてインポートするみたいです。
今回、言語設定に関してはデフォルトの英語のまま進める。
"""
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )

admin.site.register(models.User, UserAdmin)
# 8.1.2 Todo モデルの作成 / 最下部に追加
admin.site.register(models.Todo) 
