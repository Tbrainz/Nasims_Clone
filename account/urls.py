from django.urls import path 
from django.contrib.auth.views import LoginView, LogoutView
from .views import registration
from .views import dashboard
from .views import S_dashboard,DeleteProfile
from .views import Form
from .views import NewProfile

app_name = 'account'
urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name='logout'),
    path('register/', registration, name='registration'),
    path('dashboard/', dashboard, name='dashboard'),
    path('s_dashboard/', S_dashboard.as_view(), name='s_dashboard'),
    path('formview/', Form.as_view(), name='formview'),
    path('new_profile/<pk>', NewProfile.as_view(), name='new_profile'),
    path('delete/<pk>', DeleteProfile.as_view(), name='delete')
  
]