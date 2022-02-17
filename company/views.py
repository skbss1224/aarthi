from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render (request,'home.html')

def register(request):
    name=request.POST['name']
    password=request.POST['password']
    address=request.POST['address']
    mail=request.POST['mail']
    return render(request,"output.html",{'name':name,'password':password,'address':address,'mail':mail})
   




    

