from django.shortcuts import render
from django.views.generic import TemplateView

# ここから追加
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'accounts/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'accounts/login.html'
# ここまで追加



# Create your views here.
class TopView(TemplateView):
    template_name = "top.html"

    

