from django.shortcuts import render
from emailApp.models import User

# Create your views here.
def index(request):
    return render(request,"emailApp/index.html")

def index1(request):
    userDetails = User.objects.order_by('FirstName')
    my_dict={'details':userDetails}
    return render(request,"emailApp/users.html",context=my_dict)
