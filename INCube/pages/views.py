from django.shortcuts import render, render_to_response
from .models import Project
from .forms import ProjectForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf


def index(request):
    return render(request, 'pages/projectBits.html')


def new(request):
    if request.POST:
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            print("valid")
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ProjectForm()
   
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('pages/NewsFeed.html', args)


def view(request): 
    project_data = Project.objects.all()
    return render(request, 'pages/feedPage.html', {'project_data': project_data})


def dev(request):
    return render(request, 'pages/developers.html')
