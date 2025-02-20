from django.http import HttpResponse
#Response le skte ho
from django.shortcuts import render
#methods
def home(request):
    #ek request par home return karna h
    #return HttpResponse("Hello World, you are at homepage")
    return render(request, 'website/index.html')
def about(request):
    #ek request par home return karna h
    return HttpResponse("Hello World, you are at aboutpage")

def contact(request):
    #ek request par home return karna h
    return HttpResponse("Hello World, you are at contactpage")