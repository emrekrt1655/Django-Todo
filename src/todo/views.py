from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoAddForm
def home(request):
    return render(request, "todo/home.html")

def todo_list(request):
    todos =  Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, "todo/todo_list.html", context)

def todo_create(request):
    form = TodoAddForm()
    if request.method == "POST":
        form = TodoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo-list")
    context = {
        'form': form
    }
    return render(request, "todo/todo_create.html", context)
    