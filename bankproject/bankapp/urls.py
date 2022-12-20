from . import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout', views.logout, name='logout'),
    path('bank', views.bank, name='bank'),
    path('message', views.message, name='message'),

]