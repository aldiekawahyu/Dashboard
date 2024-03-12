
from django.shortcuts import render


# Create your views here.
# def index(request):
#     return render(request, "landing_page/login.html")

def login(request):

    # Melewatkan JSON ke template
    return render(request, 'login_page/login.html')
