from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'user'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('sign-up/', views.CreateView.as_view(), name='sign-up'),
    path('update/', views.UpdateView.as_view(), name='update'),
    path('update/password', views.PasswordChangeView.as_view(), name='password'),
    path('update/delete', views.DeleteView.as_view(), name='delete'),

    path('creater/application/', views.CreaterApplicationView.as_view(), name='creater-application'),
    path('creater/update/', views.CreaterUpdateView.as_view(), name='creater-update'),
]