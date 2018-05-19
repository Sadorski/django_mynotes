from django.shortcuts import render, HttpResponse, redirect
from models import Note
  # the index function is called when root is visited
def index(request):
    context = {
        'notes': Note.objects.all()
    }
    return render(request, 'notes/index.html', context)

def process(request):
    if request.method == 'POST':
        if request.POST['action'] == 'addtitle':
            Note.objects.create(title=request.POST['title'], desc="Enter description here...")
        if request.POST['action'] == 'delete':
            Note.objects.get(id=request.POST['noteid']).delete()
        if request.POST['action'] == 'editnote':
            a = Note.objects.get(id=request.POST['noteid'])
            a.desc = request.POST['note']
            a.save()
    return redirect('/')
   