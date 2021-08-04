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

test01 = {1:"東京都",2:"神奈川県",3:"埼玉県",4:"茨城県",5:"栃木県",6:"群馬県",7:"北海道",8:"青森県",9:"岩手県",10:"宮城県"
,11:"秋田県",12:"山形県",13:"福島県",14:"新潟県",15:"富山県",16:"石川県",17:"福井県",18:"山梨県",19:"長野県",20:"岐阜県"
,21:"静岡県",22:"愛知県",23:"三重県",24:"滋賀県",25:"京都府",26:"大阪府",27:"兵庫県",28:"奈良県",29:"和歌山県",30:"鳥取県"
,31:"島根県",32:"岡山県",33:"広島県",34:"山口県",35:"徳島県",36:"香川県",37:"愛媛県",38:"高知県",39:"福岡県",40:"佐賀県"
,41:"長崎県",42:"熊本県",43:"大分県",44:"宮崎県",45:"鹿児島県",46:"千葉県",47:"沖縄県"}

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
        if photo_get == None:
            photo_get = 'media/20200501_noimage_7tkYzwv.png'
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


def maps(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    url_id = request.path
    login_user_id = request.user.id
    error = 'no data'
    text = re.sub(r"[a-z]", "", url_id)
    text = text.replace("/","")
    a = str(user_id)
    keys = int(text.replace(a,"",1))
    prefects = test01[keys]
    sort = Visit.objects.filter(prefecture__exact = test01[keys],author_id = user_id)
    
    if int(login_user_id) == int(user_id):
        None
    else:
        raise Http404("権限がありません")

    if sort.count() >= 1:
        error = ""
    params = {
        'prefects':prefects,
        'user':user,
        'data':sort,
        'error':error,
    }
    return render(request, 'eventmap/maps.html', params)
    
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
