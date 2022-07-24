# 3.10.4 /user/urls.py を /todo_project/urls.py にルーティング
from django.contrib import admin
from django.urls import path, include           # 3.10.5 追加

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('api/user/', include('user.urls')), # 3.10.6 追加
    # 8.3.2 Todo app の作成 / url の作成
    path('api/', include('todo.urls')), 
]
