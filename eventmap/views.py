from collections import Counter
from functools import update_wrapper
from django import views
from django.core.files import uploadedfile
from django.db.models.base import Model
from django.db.models.expressions import F, Func
from django.db.models.fields.files import ImageField
from django.db.models.query import Prefetch
from django.db import models
from django.forms.fields import BooleanField
from django.forms.forms import Form
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, request, QueryDict
from django.utils.translation import deactivate, ugettext
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView
from .forms import LoginForm, SignUpForm, UserForm, ConectForm, Visiter
from django.views import generic
from . import models
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView) 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Visit
from logging import Logger
import re
from django.core.mail import BadHeaderError, send_mail
# Create your views here.


class Login(LoginView):
    form_class = LoginForm
    template_name = 'eventmap/login.html'
    def get_redirect_url(self):
        user_id = self.request.user.id
        settings.LOGIN_REDIRECT_URL = '/eventmap/'+str(user_id)
    
class Top(LoginRequiredMixin, generic.TemplateView):
    template_name = 'eventmap/map.html'
    redirect_field_name = 'redirect_to'
    
    def get_context_data(self, **kwargs):
        url_id = self.request.path
        user_id = self.request.user.id
        form = UserForm()
        
        if int(user_id) == int(url_id[-1]):
            None
        else:
            raise Http404("権限がありません")

        
        location = Visit.objects.values('prefecture').filter(author_id = user_id)
        prefect_all = ""
        spot = 0
        for i in location:
            
            prefect_list = i.get('prefecture')
            if re.search(prefect_list, prefect_all) != None:
                None
            else:   
                prefect_all += prefect_list + " "
                spot += 1
                
        params = {
            'form':form,
            'color':prefect_all,
            'spot':spot,
        }
        return (params)
        
    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST, request.FILES)
        
        check = request.POST.get('public')
        
        prefecture_get = form.data['prefecture']
        place_get = form.data['place']
        year = form.data['startrip_year']
        month = form.data['startrip_month']
        day = form.data['startrip_day']
        yeara = form.data['endtrip_year']
        montha = form.data['endtrip_month']
        daya = form.data['endtrip_day']
        photo_get = form.files.get('photo')
        comment_get = form.data['comment']
        author_get = self.request.user
        
        if check == None:
            Visit.objects.create(
                prefecture = prefecture_get,
                place = place_get,
                startrip = year+'-'+month+'-'+day,
                endtrip = yeara+'-'+montha+'-'+daya,
                photo = photo_get,
                comment = comment_get,
                author = author_get,
            )
        else:
            check = True
            Visit.objects.create(
                prefecture = prefecture_get,
                place = place_get,
                startrip = year+'-'+month+'-'+day,
                endtrip = yeara+'-'+montha+'-'+daya,
                photo = photo_get,
                public = check,
                comment = comment_get,
                author = author_get,
            )
            
            
            
        
        
        return self.get(request, *args, **kwargs)
    
class Logout(LogoutView):
    template_name = 'eventmap.html'
   

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

def log1(request, user_id):
    #user_idがurlの入力によって変動するのでログインユーザーチェックの際は別の変数を用いる
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '東京都',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-7]):
        None
    else:
        raise Http404("権限がありません")
    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log1.html', params)

def log2(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '神奈川県',author_id = user_id)
    
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-7]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log2.html', params)

def log3(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '埼玉県',author_id = user_id)

    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-7]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log3.html', params)

def log4(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '茨城県',author_id = user_id)

    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-7]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log4.html', params)

def log5(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '栃木県',author_id = user_id)

    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-7]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log5.html', params)

def log6(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '群馬県',author_id = user_id)

    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-7]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log6.html', params)

def log7(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '北海道',author_id = user_id)

    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-7]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log7.html', params)

def log8(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '青森県',author_id = user_id)

    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-7]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log8.html', params)

def log9(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '岩手県',author_id = user_id)

    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-7]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log9.html', params)

def log10(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '宮城県',author_id = user_id)

    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log10.html', params)

def log11(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '秋田県',author_id = user_id)

    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log11.html', params)

def log12(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '山形県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log12.html', params)

def log13(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '福島県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log13.html', params)

def log14(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '新潟県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log14.html', params)

def log15(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '富山県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log15.html', params)

def log16(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '石川県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log16.html', params)

def log17(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '福井県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log17.html', params)

def log18(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '山梨県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log18.html', params)

def log19(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '長野県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log19.html', params)

def log20(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '岐阜県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log20.html', params)

def log21(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '静岡県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log21.html', params)

def log22(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '愛知県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log22.html', params)

def log23(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '三重県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log23.html', params)

def log24(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '滋賀県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log24.html', params)

def log25(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '京都府',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log25.html', params)

def log26(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '大阪府',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log26.html', params)

def log27(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '兵庫県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log27.html', params)

def log28(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '奈良県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log28.html', params)

def log29(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '和歌山県', author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    
    return render(request, 'eventmap/log29.html', params)

def log30(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '鳥取県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log30.html', params)

def log31(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '島根県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log31.html', params)

def log32(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '岡山県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log32.html', params)

def log33(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '広島県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log33.html', params)

def log34(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '山口県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log34.html', params)

def log35(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '徳島県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log35.html', params)

def log36(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '香川県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log36.html', params)

def log37(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '愛媛県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log37.html', params)

def log38(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '高知県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log38.html', params)

def log39(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '福岡県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log39.html', params)

def log40(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '佐賀県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log40.html', params)

def log41(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '長崎県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log41.html', params)

def log42(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '熊本県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log42.html', params)

def log43(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '大分県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log43.html', params)

def log44(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '宮崎県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log44.html', params)

def log45(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '鹿児島県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log45.html', params)

def log47(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '沖縄県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log47.html', params)

def log46(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    error = 'no data'
    test = Visit.objects.filter(prefecture__exact = '千葉県',author_id = user_id)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-8]):
        None
    else:
        raise Http404("権限がありません")

    if test.count() >= 1:
        error = ""
    params = {
        'user':user,
        'data':test,
        'error':error,
    }
    return render(request, 'eventmap/log46.html', params)

def forms(request):
    params = {
        'title':'フォーム',
        'msg':'お問い合わせ用フォーム',
        'sample':'sample',
        'form':ConectForm(),
    }
    if request.method == 'POST':
        fork = ConectForm(request.POST)
        
        if fork.is_valid():
            
            subject = fork.cleaned_data['subject']
            name = fork.cleaned_data['name']
            from_mail = fork.cleaned_data['mail']
            message = fork.cleaned_data['text']
            recipients = [settings.EMAIL_HOST_USER]
            
            message = message + '<br>お名前：　' +name+ '<br>メールアドレス：　' +from_mail
            
            send_mail(subject, message, from_mail, recipients, html_message=message)
            return redirect('forms')
    return render(request, 'eventmap/forms.html', params)

def howto(request):
    return render(request, 'eventmap/howto.html')

def edit(request,num,user_id):
    
    obj = Visit.objects.get(id=num)
    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-1]):
        None
    else:
        raise Http404("権限がありません")

    if (request.method == 'POST'):
        
        formss = Visiter(request.POST,request.FILES, instance=obj)
        formss.save()
        return redirect('map',user_id)
        
    params = {
        'id':num,
        'form': Visiter(instance=obj),
    }
    return render(request,'eventmap/edit.html',params)

def delete(request, num, user_id):
    obj = Visit.objects.get(id=num)

    url_id = request.path
    login_user_id = request.user.id
    
    if int(login_user_id) == int(url_id[-1]):
        None
    else:
        raise Http404("権限がありません")
    if (request.method == 'POST'):
        obj.delete()
        
        return redirect('map',user_id)

    params = {
        'id':num,
        'obj':obj,
    }
    return render(request, 'eventmap/delete.html', params)
        
def public(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    data = ""
    error = 'no data'
    test = Visit.objects.filter(public = True)

    if test.count() >= 1:
        data = test
        error = ""
    params = {
        'data':data,
        'error':error,
    }
    return render(request, 'eventmap/public.html', params)

def news(request):
    return render(request, 'eventmap/news.html')