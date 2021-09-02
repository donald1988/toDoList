from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import ToDo


# Create your views here.

def listItems(request):
    context = {'todo_list' : ToDo.objects.all()}
    return render(request, 'todoList/todo_list.html', context)

def insert(request:HttpRequest):
    todo = ToDo(content = request.POST['content'])
    todo.save()
    return redirect('/todoList/list/') 

def delete(requet, todo_id):
    todo = ToDo.objects.get(id = todo_id)
    todo.delete()
    return redirect('/todoList/list/')
