from django.urls import path
from . import views

app_name = 'crud'
urlpatterns = [
    path('', views.home, name='home'),
    path('education/', views.education, name='education'),
    path('experience/', views.experience, name='experience'),
    path('message/', views.message, name='message'),
    path('contact/', views.contact, name='contact'),

]