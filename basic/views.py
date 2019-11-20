#from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .models import Team
from .forms import LoginForm

# Create your views here.


@login_required
def office_view(request):
    '''
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return HttpResponseRedirect('/login')
    '''
    #team = Team.objects.get(id=request.user.id)
    team = Team.objects.filter(id=request.user.id).first()
    return render(request, 'office.html',
                  {"team": team,
                   })


class SignUp(generic.CreateView):
    User = get_user_model()
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

