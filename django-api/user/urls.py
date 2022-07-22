from django.urls import path

from user import views


app_name = 'user'

# as_view() = View の条件を満たす関数を自動で実行してくれる
urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    # トークンの発行 
    path('token/', views.CreateTokenView.as_view(), name='token'), 
    # ユーザー情報の更新
    path('update/', views.ManageUserView.as_view(), name='update'), 
]