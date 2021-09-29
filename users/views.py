from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


# Create your views here.
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        image = request.POST['image']
        phone = int(phone)
        if password1 != password2:
            message = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone': phone,
                'message_from_password': 'Password is not matching. Please try again...'
            }
            return render(request, template_name='users/signup.html', context=message)
        elif User.objects.filter(username=email).exists():
            message = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone': phone,
                'message_from_email': 'This email use for another account. Please use another or login using this email.'
            }
            return render(request, template_name='users/signup.html', context=message)
        else:
            user = User(username=email, first_name=first_name, last_name=last_name, email=email,
                        password=password1)
            user.save()
            profile = Profile(user=user, profile_picture=image, phone=phone)
            profile.save()
            new_user = authenticate(username=email, password=password1)
            login(new_user)
            return redirect('users:profile')


    else:
        return render(request, template_name='users/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(user)
            return redirect('users:profile')
        else:
            message = {
                'username': username,
                'message_from_login': 'Your Email or Passowrd is incorrect.'
            }
            return render(request, template_name='users/login.html', context=message)
    else:
        return render(request, template_name='users/login.html')


def logout(request):
    logout(request)
    return redirect('app:home')


def profile(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email
    phone = request.user.profile.phone
    image = request.user.profile.profile_picture
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'image': image
    }
    return render(request, template_name='user/PublicProfile.html', context=data)
