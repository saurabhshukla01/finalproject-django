from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import userform
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method=='POST':
        form1=userform(request.POST)
        if form1.is_valid():
            username=form1.cleaned_data['username']
            first_name = form1.cleaned_data['first_name']
            last_name = form1.cleaned_data['last_name']
            email = form1.cleaned_data['email']
            password = form1.cleaned_data['password']
            User.objects.create_user(username=username,
			first_name=first_name,last_name=last_name,
            email=email,password=password)
            messages.success(request,f'Hello {username} Your Request Has been Posted.')
            return redirect('login')
    else:
        form1=userform()	
    context = {'form':form1}
    return render(request,'registration.html',context)

def logoutuser(request):
	logout(request)
	return render(request,'login.html')   	




def loginuser(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if  user.is_staff:    
                login(request,user)
                return HttpResponse("<h1>WelCome</h1>")
            else:
                return HttpResponse("<h1>Wait for Permissions.</h1>")    
        else:
            return HttpResponse('<h1>invalid</h1>')   
    else:    
        return render(request,'login.html')	