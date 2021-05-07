from django.urls import path
from . import views
from .forms import LoginForm


urlpatterns = [
    path('eventmap/', views.Top.as_view(), name='map'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('entry/', views.entry, name='entry'),
    path('users/<int:user_id>/', views.users, name='users'),
]