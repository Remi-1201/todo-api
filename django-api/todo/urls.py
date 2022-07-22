# 8.3.1 Todo app の作成 / url の作成
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todo import views

""" DefaultRouter = Router を登録できるのは ViewSet に限ります。
Router は詳細な API（/todo/1/ とか /todo/4/）を自動的に付加して URL 登録してくれます"""
router = DefaultRouter()
router.register('todo', views.TodoViewSet)

app_name = 'todo'

urlpatterns = [
    path('', include(router.urls))
]