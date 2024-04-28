from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from myapp.forms import SignUpForm
from .models import Goods


class HomePage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goods'] = Goods.objects.all()
        return context


class MyLogin(LoginView):
    template_name = 'signin.html'


class MyRegister(CreateView):
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    form_class = SignUpForm


class MyLogOut(LogoutView):
    template_name = 'signout.html'
