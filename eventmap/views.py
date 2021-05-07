from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from django.views import generic
from . import models
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView) 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# Create your views here.


class Login(LoginView):
    form_class = LoginForm
    template_name = 'eventmap/login.html'


class Logout(LogoutView):
    template_name = 'eventmap.html'

class Top(LoginRequiredMixin, generic.TemplateView):
    template_name = 'eventmap/map.html'
    redirect_field_name = 'redirect_to'

def entry(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            mail = form.cleaned_data.get('email')
            from_mail = settings.EMAIL_HOST_USER
            message = 'ログインページからログインしてご利用ください'
            subject = 'ユーザー登録ありがとうございます！'
            recipients = [mail]
            
            user = authenticate(username=username, password = raw_password)
            login(request, user)
            send_mail(subject, message, from_mail, recipients, html_message=message)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'eventmap/entry.html', {'form':form})

def users(request, user_id):
	user = get_object_or_404(User, pk=user_id)
	params = {
		'user': user,
	}
	return render(request, 'eventmap/users.html', params)
    