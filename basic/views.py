from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from .models import TodoItem

from .forms import LoginForm

# Create your views here.


def office_view(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return HttpResponseRedirect('/login')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
