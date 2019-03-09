from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request,*args,**kwargs):
	print(args,kwargs)
	print(request.user)
	#return HttpResponse("<h1>HEllo World</h1>")
	return render(request , "home.html",{})

def contact_view(request,*args,**kwargs):
	#return HttpResponse("<h3>this is contact page</h3>")
	return render(request , "contact.html",{})
def about_view(request,*args,**kwargs):
	#return HttpResponse("<h3>this is about page</h3>")
	return render(request , "about.html",{})
