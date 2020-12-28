from django.shortcuts import render
from .models import Todo
def home(request):
    return render(request, "todo/home.html")

def todo_list(requset):
    todos =  Todo.objects.all()
    