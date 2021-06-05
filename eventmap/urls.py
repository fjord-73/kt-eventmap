from django.urls import path
from . import views
from .forms import LoginForm


urlpatterns = [
    
    path('kt-eventmap/<int:user_id>', views.Top.as_view(), name='map'), #関数が必要
    path('kt-eventmap/login/', views.Login.as_view(), name='login'),
    path('kt-eventmap/logout/', views.Logout.as_view(), name='logout'),
    path('kt-eventmap/entry/', views.entry, name='entry'),
    path('kt-eventmap/<int:user_id>/1/log', views.log1, name='log1'),
    path('kt-eventmap/<int:user_id>/2/log', views.log2, name='log2'),
    path('kt-eventmap/<int:user_id>/3/log', views.log3, name='log3'),
    path('kt-eventmap/<int:user_id>/4/log', views.log4, name='log4'),
    path('kt-eventmap/<int:user_id>/5/log', views.log5, name='log5'),
    path('kt-eventmap/<int:user_id>/6/log', views.log6, name='log6'),
    path('kt-eventmap/<int:user_id>/7/log', views.log7, name='log7'),
    path('kt-eventmap/<int:user_id>/8/log', views.log8, name='log8'),
    path('kt-eventmap/<int:user_id>/9/log', views.log9, name='log9'),
    path('kt-eventmap/<int:user_id>/10/log', views.log10, name='log10'),
    path('kt-eventmap/<int:user_id>/11/log', views.log11, name='log11'),
    path('kt-eventmap/<int:user_id>/12/log', views.log12, name='log12'),
    path('kt-eventmap/<int:user_id>/13/log', views.log13, name='log13'),
    path('kt-eventmap/<int:user_id>/14/log', views.log14, name='log14'),
    path('kt-eventmap/<int:user_id>/15/log', views.log15, name='log15'),
    path('kt-eventmap/<int:user_id>/16/log', views.log16, name='log16'),
    path('kt-eventmap/<int:user_id>/17/log', views.log17, name='log17'),
    path('kt-eventmap/<int:user_id>/18/log', views.log18, name='log18'),
    path('kt-eventmap/<int:user_id>/19/log', views.log19, name='log19'),
    path('kt-eventmap/<int:user_id>/20/log', views.log20, name='log20'),
    path('kt-eventmap/<int:user_id>/21/log', views.log21, name='log21'),
    path('kt-eventmap/<int:user_id>/22/log', views.log22, name='log22'),
    path('kt-eventmap/<int:user_id>/23/log', views.log23, name='log23'),
    path('kt-eventmap/<int:user_id>/24/log', views.log24, name='log24'),
    path('kt-eventmap/<int:user_id>/25/log', views.log25, name='log25'),
    path('kt-eventmap/<int:user_id>/26/log', views.log26, name='log26'),
    path('kt-eventmap/<int:user_id>/27/log', views.log27, name='log27'),
    path('kt-eventmap/<int:user_id>/28/log', views.log28, name='log28'),
    path('kt-eventmap/<int:user_id>/29/log', views.log29, name='log29'),
    path('kt-eventmap/<int:user_id>/30/log', views.log30, name='log30'),
    path('kt-eventmap/<int:user_id>/31/log', views.log31, name='log31'),
    path('kt-eventmap/<int:user_id>/32/log', views.log32, name='log32'),
    path('kt-eventmap/<int:user_id>/33/log', views.log33, name='log33'),
    path('kt-eventmap/<int:user_id>/34/log', views.log34, name='log34'),
    path('kt-eventmap/<int:user_id>/35/log', views.log35, name='log35'),
    path('kt-eventmap/<int:user_id>/36/log', views.log36, name='log36'),
    path('kt-eventmap/<int:user_id>/37/log', views.log37, name='log37'),
    path('kt-eventmap/<int:user_id>/38/log', views.log38, name='log38'),
    path('kt-eventmap/<int:user_id>/39/log', views.log39, name='log39'),
    path('kt-eventmap/<int:user_id>/40/log', views.log40, name='log40'),
    path('kt-eventmap/<int:user_id>/41/log', views.log41, name='log41'),
    path('kt-eventmap/<int:user_id>/42/log', views.log42, name='log42'),
    path('kt-eventmap/<int:user_id>/43/log', views.log43, name='log43'),
    path('kt-eventmap/<int:user_id>/44/log', views.log44, name='log44'),
    path('kt-eventmap/<int:user_id>/45/log', views.log45, name='log45'),
    path('kt-eventmap/<int:user_id>/46/log', views.log46, name='log46'),
    path('kt-eventmap/<int:user_id>/47/log', views.log47, name='log47'),
    path('kt-eventmap/forms', views.forms, name='forms'),
    path('kt-eventmap/howto', views.howto, name='howto'),
    
]