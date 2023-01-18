

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('count/', views.count, name='count'), #the name count is passed in he url (home.html)
    path('about/', views.aboutpage, name='about'),

]
