from django.urls import path
from .views import home, todo_list, todo_create

urlpatterns = [
    path("", home, name='home'),
    path("list/", todo_list, name='todo-list'),
    path("create/", todo_create, name='todo-create')
]