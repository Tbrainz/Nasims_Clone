from django.urls import path 
from .views import Contact, About, News, Index

urlpatterns = [
    path('contact/', Contact.as_view(), name='contact'),
    path('about/', About.as_view(), name='about'),
    path('news/', News.as_view(), name='news'),
    path('', Index.as_view(), name='home')
]