from django.shortcuts import render,HttpResponseRedirect
from .models import TodoData
from .forms import TodoForm
#my url

def home(request):
    if request.method == 'POST':
        show_Input = TodoForm(request.POST)
        if show_Input.is_valid():
            show_Input.save()
            return HttpResponseRedirect('/')

    show_Input = TodoForm()
    todo_list = TodoData.objects.all()

    return render(request,'todo-tem/index.html',{'Todo':show_Input,'todo_list':todo_list})




def delete_item(request, id):
    TodoData.objects.get(id=id).delete()
    return HttpResponseRedirect('/')