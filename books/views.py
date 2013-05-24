from django.db.models import Q
from django.shortcuts import render_to_response
from models import Person

def search(request):
	query = request.GET.get('q', '')
	if query:
		qset = (
			Q(first_name__icontains=query) |
			Q(last_name__icontains=query)
		)
		results = Person.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response('search.html', {"results": results,"query": query})
