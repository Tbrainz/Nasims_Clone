from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from account.models import Profile

# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'


class Contact(TemplateView):
    template_name = 'contact.html'

class News(ListView):
    template_name = 'news.html'
    model = Profile
    context_object_name = 'users'

class About(TemplateView):
    template_name = 'about.html'
