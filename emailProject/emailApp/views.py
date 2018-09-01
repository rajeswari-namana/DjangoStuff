from django.shortcuts import render
#from emailApp.models import User
from emailApp.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request,"emailApp/index.html")

def index1(request):
    form=NewUserForm()

    if request.method=="POST":
        form=NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Form invalid")

    return render(request,'emailApp/users.html',{'form':form})
