from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
# Create your views here.

def index(request):
    return render(request,"blog/index.html")

def detail(reqest):
    return HttpResponse("detale page")

class AccountCreateView(View):
    def get(self,request):
        return render(request,"blog/register.html")
    def post(self,request):
        User.objects.create_user(
            username=request.POST["username"],
            password=request.POST["password"],
        )
        return render(request,"blog/register_success.html")

class AccountLoginView(LoginView):
    template_name = "blog/login.html"
    def get_default_redirect_url(self):
        return "/blog"