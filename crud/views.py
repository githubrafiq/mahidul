from django.shortcuts import render
from .models import Education, Experience, Details

# Create your views here.





context = {
    'educations': Education.objects.all(),
    'experiences': Experience.objects.all(),
    'details': Details.objects.all(),
}


def home(request):
    return render(request, 'crud/index.html', context)


def education(request):
    return render(request, 'crud/education.html', context)


def experience(request):
    return render(request, 'crud/experience.html', context)


def message(request):
    return render(request, 'crud/message.html', context)


def contact(request):
    return render(request, 'crud/contact.html', context)
