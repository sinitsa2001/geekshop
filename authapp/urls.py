from django.urls import path

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('register/', authapp.register, name='register'),
    path('profile/', authapp.profile, name='profile'),
    path('logout/', authapp.logout, name='logout'),

    path('verify/<email>/<activation_key>', authapp.verify, name = 'verify'),

]