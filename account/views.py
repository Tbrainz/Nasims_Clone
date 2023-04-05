from django.shortcuts import render
from .forms2 import Register
from .models import Profile
from .forms2 import RegisterProfile
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


class Form(CreateView):
    template_name = 'register.html'
    form_class = Register
    success_url = '/login'


def registration(request):
   
    form2 = Register(request.POST or None)
    if request.method == 'POST':
        form2 = Register(request.POST or None)
        if form2.is_valid():
            form2.save()
            return redirect('/dashboard')
        else:
            form2 = Register(request.POST or None)
   
    return render(request, 'register.html', {'form': form2})

def dashboard(request):
    context = Profile.objects.values().all()
    
    return render(request, 'dashboard.html', {'context':context})

class S_dashboard(LoginRequiredMixin, TemplateView):
    template_name = 's_dashboard.html'
    login_url = '/login/'

class NewProfile(SuccessMessageMixin, UpdateView):
    template_name = 'new_profile.html'
    form_class = RegisterProfile
    model = Profile
    success_message = 'Profile updated successfully'
    success_url = '/s_dashboard'

    # def get_success_url(self) -> str:
    #     return reverse('account:s_dashboard', kwargs = {'pk':self.get_object().pk})



class DeleteProfile(DeleteView):
    template_name = 'delete.html'
    model = Profile
    context_object_name = 'profile'
    success_url = 'dashboard'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Profile
        return context
    