from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<em>My Second App</em>")

# Create your views here.
def help(request):
    dict_two={'help_text':"hey need some help"}
    return render(request,"AppTwo/index.html",context=dict_two)
