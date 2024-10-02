from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import ToDoViewSet, documentation_view

router = DefaultRouter()
router.register(r'todos', ToDoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', documentation_view, name='documentation_index'),
    re_path(r'^docs/(?P<path>.*)$', documentation_view, name='documentation'),
]
