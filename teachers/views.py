from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import os, traceback, sys
from teachers.models import Teachers, School
import json
from other import clean_demo, clean_matched
from django.conf import settings
from django.template import Library
from django import template

register = Library()
register.filter('media')

def index(request):
	return render_to_response('base.html')

def metatest(request):
	values = request.META.items()
	values.sort()
	html = []
	for k,v in values:
			html.append("<tr><td>%s</td><td>%s</td></tr>"%(k,v))
	return HttpResponse("<table>%s</table>"%"\n".join(html))

def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	error = False
	if 'school' in request.GET:
		query = request.GET['school']
		if not query:
			error = False
			return render_to_response('base.html',{'error': error})
		else:
			schools = School.objects.filter(name__icontains=query)
			if not schools:
				error = True
				return render_to_response('base.html',{'error': error})
			else:
				return render_to_response('base_search.html',{'schools':schools, 'query':query, 'error': error})
	else:
		return render_to_response('base.html',{'error': error})


def teacher(request, dbn, teacher_id):
	teacher = Teachers.objects.get(id=teacher_id)
	school = School.objects.get(dbn=dbn)
	return render_to_response('base_teacher.html',{'teacher': teacher, 'school': school})

def school(request, dbn):
	error = False
	school = School.objects.get(dbn=dbn)
	try:
		teachers = Teachers.objects.filter(dbn=school)
	except:
		error = True

	if not teachers:
		error = True

	return render_to_response('base_school.html', {'school': school, 'teachers':teachers, 'error': error})

def load(request):
	clean_matched.main()
	clean_demo.main()
	loadhtml = "<html><body>LOAD SUCCESFUL!</body></html>"
	return HttpResponse(loadhtml)

def drop(request):
	Teachers.objects.all().delete()
	School.objects.filter(dbn__icontains = "1").delete()
	School.objects.filter(dbn__icontains = "2").delete()
	School.objects.filter(dbn__icontains = "3").delete()
	School.objects.filter(dbn__icontains = "4").delete()
	School.objects.filter(dbn__icontains = "5").delete()
	School.objects.filter(dbn__icontains = "6").delete()
	School.objects.filter(dbn__icontains = "7").delete()
	School.objects.filter(dbn__icontains = "8").delete()
	School.objects.filter(dbn__icontains = "9").delete()
	
	loadhtml = "<html><body>DROP SUCCESSFUL!</body></html>"
	return HttpResponse(loadhtml)


@register.filter
def media(file):
    '''
    Concatenate MEDIA_URL and file.
    '''

    return settings.BASE_URL + file
