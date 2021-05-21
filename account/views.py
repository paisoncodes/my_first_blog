from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm
from articles.models import BlogPost


def registration_view(request):
    context={}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)

def login_view(request):
    context={}

    user = request.user
    if user.is_authenticated:
        return redirect('home')
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AccountAuthenticationForm
    
    context['login_form'] = form
    return render(request, 'account/login.html', context)


def logout_request(request):
	logout(request)
	return redirect("home")

def account_view(request):

    user = request.user
    if not user.is_authenticated:
        return redirect('home')
    
    context = {}
    
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.initial={
                'email': request.POST['email'],
                'username': request.POST['username']
            }
            form.save()
            context['success_message'] = 'Update Successful!'
    else:
        form = AccountUpdateForm(
            initial={
                'email': user.email,
                'username': user.username
            }
        )
    
    context['account_form'] = form

    blog_posts = BlogPost.objects.filter(author=user)
    context['blog_posts'] = blog_posts

    return render(request, 'account/account.html', context)



def must_authenticate_view(request):
    return render(request, 'account/must_authenticate.html', {})