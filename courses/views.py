from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
def TutorialListView(request):
	context = {}
	context['tutorials'] = Tutorial.objects.all()

	return render(request,'course_list.html', context)

@login_required(login_url="/users/login/")
def TutorialDetailView(request,id=None):
	if  request.user.is_authenticated:
		context = {}
		login_url = 'login'
		tutorial = Tutorial.objects.get(id=id)
		context['tutorial'] = tutorial
		context['terminals'] = Terminal.objects.get(tutorial=tutorial)

		return render(request,'course_detail.html', context)
	return render(request,'registration/login.html')