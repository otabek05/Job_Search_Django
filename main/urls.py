from django.urls import path
from . import views

urlpatterns= [
    path('',views.main, name='home'),
    path('jobCreate/', views.createJob, name='elon'),
    path('find/<int:id>/', views.category, name='category'),
    path('filter/<int:id>/', views.location, name='location'),
    path('found/', views.search, name='search'),
    path('details/<int:id>/', views.details, name='details'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),

]