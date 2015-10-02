from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import Template, Context

import json

@csrf_exempt
def showHouses(request):
	if request.method == 'POST':
		try:
			location1 = request.POST['1']
			location2 = request.POST['2']
			location3 = request.POST['3']
