from django.contrib import admin
from django.urls import path, include           # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    #/user/urls.py を /todo_project/urls.py にルーティング
    path('api/user/', include('user.urls')), 
    # 8.3.2 Todo app の作成 / url の作成
    path('api/', include('todo.urls')), 
]
