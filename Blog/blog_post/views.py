from django.shortcuts import render

# Create your views here.

def index_view(request):

	index_dict = {
		
	}
	
	return render(request,"index.html",index_dict)
