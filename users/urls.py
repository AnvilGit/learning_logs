from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/userlogin.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='users/userlogin.html'), name='logout'),
    path('register/', views.register, name='register'),
]