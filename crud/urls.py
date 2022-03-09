from django.urls import path
from . import views

app_name = 'crud'
urlpatterns = [
    path('', views.home, name='home'),
    path('education/', views.education, name='education'),
    path('experience/', views.experience, name='experience'),
    path('message/', views.message, name='message'),
    path('contact/', views.contact, name='contact'),

    path('create_edu/', views.create_edu, name='create_edu'),
    path('create_experience/', views.create_experience, name='create_experience'),
    path('create_contact/', views.create_contact, name='create_contact'),

]