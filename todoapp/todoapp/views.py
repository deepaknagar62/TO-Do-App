from django.http import *
from django.shortcuts import render,redirect
from users.models import Tasks



def Home(request):
     if request.method == "POST":
        task_description = request.POST.get('taskInput')

        if task_description:
            
            Tasks.objects.create(task=task_description)

            return redirect('home')

    
     all_tasks = Tasks.objects.all()
     return render(request, "home.html", {'all_tasks': all_tasks})  
  
            
def delete_task(request ,taskid):
    toDelete = Tasks.objects.get(pk=taskid)
    toDelete.delete()
    return redirect('home')
       

def update_task(resquest, taskid):
    task =Tasks.objects.get(pk=taskid) 
    return render(resquest, "updatepage.html",{'task': task})      


def do_update_task(request,taskid):
    if request.method == "POST":
        task_description = request.POST.get('taskInput2')
        t = Tasks.objects.get(pk=taskid)
        t.task = task_description
        t.save()
        return redirect('home')
        
    return HttpResponseBadRequest("Invalid request")
    