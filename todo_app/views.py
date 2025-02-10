from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('Title')
        description = request.POST.get('Description')
        if title and description:  # Add validation
            Todo.objects.create(
                title=title,
                description=description
            )
        return redirect('/')  # Redirect to the main page after creation
    return redirect('/')

def complete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.completed = True
    todo.save()
    return redirect('/')

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('/')
    