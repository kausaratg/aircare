from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.






def signup(request):

# collecting data frompostmethod
    if request.method == 'POST':
        username = request.POST ['username']
        FirstName=  request.POST ['FirstName']
        LastName = request.POST ['LastName']
        email =  request.POST ['email']
        password =  request.POST ['password1']
        password2 =  request.POST ['password2']

# checking if user already exit
        if User.objects.filter(username=username):
            messages.error(request, "Username already Exist!")
            return redirect('signup')
        
# checking if email already exit
        if User.objects.filter(email = email):
            messages.error(request, "Email already Exist!")
            return redirect('signup')
        
 # checking if password match already exit
        if password != password2:
            messages.error(request, "Password does not match!")
            return redirect('signup')
#creating  user info into database
        app_user_info = User.objects.create_user(username, email, password)
        app_user_info.first_name = FirstName
        app_user_info.last_name = LastName

#saving user info into database
        app_user_info.save()
# if user info is successfully created display this
        messages.success(request,'Your Account Is Successfully Created')

        # redirect the User to homepage

        return redirect('/')

    return render(request,'authentication/signup.html')  

# some of this info has not been render in the html templates
 

# login page
def login(request):
   if request.method == "POST":
       username = request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(username=username, password=password)
       if user is not None:
           auth.login(request, user)
           messages.success(request, 'successfully login')
           return redirect('/')
       else:
           messages.error(request, "invalid username or password")
           return redirect('login')
   else:
        return render(request, 'authentication/login.html')
