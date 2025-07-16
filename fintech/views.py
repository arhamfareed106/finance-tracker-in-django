from django import urls
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from fintech.forms import  RegisterForm





class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'fintech/register.html', {'form': form})
    
    
    