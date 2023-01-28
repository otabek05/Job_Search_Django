from django.urls import path
from . import views

urlpatterns=[
path('login/', views.user_login, name='login'),
path('profile/', views.myprof, name='myprofile'),
path('logout/', views.user_logout, name='logout'),
path('register/', views.user_register, name='register'),
path('my_page/', views.my_announce, name='my_page'),

]