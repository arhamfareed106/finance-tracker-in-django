from django import urls
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View





class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'fintech/register.html')
    
    
    