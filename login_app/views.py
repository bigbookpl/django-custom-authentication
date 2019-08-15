from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomePageView(TemplateView):

    template_name = "index.html"

class LoginPageView(TemplateView):

    template_name = "login.html"
