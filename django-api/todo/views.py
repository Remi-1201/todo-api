from django.shortcuts import render

# 8.2.3 Todo app の作成 / View, Pagination の作成

from rest_framework import viewsets, generics, pagination, response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Todo

from todo import serializers

"""(pagination.PageNumberPagination) = デフォルトでは1ページで全件取得してしまうため、
ページネーション機能を追加して1ページあたりの取得件数を制限します。"""
class TodoPagination(pagination.PageNumberPagination):
    # Get 2 Todo items in a page
    page_size = 2

    def get_paginated_response(self, data):
        # response.Response の中身は英字通りで、デフォルトよりちょっと見栄えがよくなります
        return response.Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data,
            'page_size': self.page_size,
            'range_first': (self.page.number * self.page_size) - (self.page_size) + 1,
            'range_last': min((self.page.number * self.page_size), self.page.paginator.count),
        })

# ModelViewSet = 基本的な APIView が備わっています
class TodoViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating todo items"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.TodoSerializer
    queryset = Todo.objects.order_by('-created_at')
    pagination_class = TodoPagination

    def perform_create(self, serializer):
        """Create a new Todo item"""
        serializer.save(user=self.request.user)