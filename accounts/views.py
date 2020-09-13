from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth#to pust the collected post data into the django database auth_user
# Create your views here.


def login(request):

    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):

    if request.method == 'POST':

        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        #save the data by creating an object
        if password1 == password2:
            if User.objects.filter(username=username).exists():     #to chect if the user name exists
                messages.info(request,'Username already exists')     #prints the message on the webpage
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password1)
                user.save() #saves the user
                messages.info(request,'user created')
                return redirect ('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')