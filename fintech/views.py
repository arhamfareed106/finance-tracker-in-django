from django import urls
from django.urls import path
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View
from flask import request
from fintech.forms import  RegisterForm
from django.contrib.auth import login




class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'fintech/register.html', {'form': form})
    def post(self, request, *args, **kwargs ):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=   form.save()
            login(request, user)
            redirect('')
            
            
        
    
    
    