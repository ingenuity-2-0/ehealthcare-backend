from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout


# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
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
        elif User.objects.filter(email=email).exists():
            message = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone': phone,
                'username': username,
                'message_from_email': 'This email use for another account. Please use another or login using this email.'
            }
            return render(request, template_name='users/signup.html', context=message)
        elif User.objects.filter(username=username).exists():
            message = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone': phone,
                'username': username,
                'message_from_username': 'Username is taken. Please try another'
            }
            return render(request, template_name='users/signup.html', context=message)
        else:
            user = User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email)
            user.set_password(password1)
            user.save()
            profile = Profile.objects.create(user=user, profile_picture=image, phone=phone)
            profile.save()
            new_user = authenticate(request, username=username, password=password1)
            print(new_user)
            login(request, new_user)
            return redirect('users:profile')
    else:
        return render(request, template_name='users/signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('users:profile')
        else:
            message = {
                'username': username,
                'message_from_login': 'Your Email or Passowrd is incorrect.'
            }
            return render(request, template_name='users/login.html', context=message)
    else:
        return render(request, template_name='users/login.html')


def user_logout(request):
    logout(request)
    return redirect('app:home')


def profile(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email
    phone = request.user.profile.phone
    image = request.user.profile.profile_picture.url
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'image': image
    }
    return render(request, template_name='users/PublicProfile.html', context=data)
