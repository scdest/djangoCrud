from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .models import Paper
from .forms import PaperForm

def index(request):
    papers = Paper.objects.all()

    return render(request, 'main/index.html', {'title': 'Головна сторінка', 'papers': papers})


def about(request):
    return render(request, 'main/about.html')


def start(request):
    return render(request, 'main/start.html')

def new_paper(request):
    if request.method == 'POST':
        form = PaperForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = PaperForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)

def paper_view(request, id=1):
    paper = Paper.objects.get(id=id)
    return render(request, 'main/paper_view.html', {'title': 'Стаття', 'paper': paper})


def index_tab(request):
    papers = Paper.objects.all()
    return render(request, 'main/index_tab.html', {'title': 'Перелік статей', 'papers': papers})


def paper_edit(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = PaperForm()
        else:
            paper = Paper.objects.get(id=id)
            form = PaperForm(instance=paper)
        return render(request, 'main/paper_edit.html', {'form': form})
    else:
        if id == 0:
            form = PaperForm(request.POST)
        else:
            paper = Paper.objects.get(id=id)
            form = PaperForm(request.POST, instance=paper)
        if form.is_valid():
            form.save()
        return redirect('main')


def paper_delete(request, id=0):
    paper = Paper.objects.get(id=id)
    paper.delete()
    papers = Paper.objects.all()
    return render(request, 'main/index_tab.html', {'title': 'Перелік статей', 'papers': papers})