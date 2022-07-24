# 3.10.3 urls.py を新規作成
from django.urls import path

from user import views


app_name = 'user'

# 3.10.4 as_view() = View の条件を満たす関数を自動で実行してくれる
urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    # 4.3  追加/ トークンの発行 
    path('token/', views.CreateTokenView.as_view(), name='token'), 
    # ユーザー情報の更新
    path('update/', views.ManageUserView.as_view(), name='update'), 
]