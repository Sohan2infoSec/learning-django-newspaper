from django.shortcuts import render
from .models import *
# Create your views here.
def TutorialListView(request):
	context = {}
	context['tutorials'] = Tutorial.objects.all()

	return render(request,'course_list.html', context)

def TutorialDetailView(request,id=None):
	context = {}
	tutorial = Tutorial.objects.get(id=id)
	context['tutorial'] = tutorial
	print("type-",type(tutorial.content))
	context['terminals'] = Terminal.objects.get(tutorial=tutorial)

	return render(request,'course_detail.html', context)