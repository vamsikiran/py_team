from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect


def showdb(request):
		return render_to_response('db_testing.py')