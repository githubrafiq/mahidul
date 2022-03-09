from django.shortcuts import render, redirect
from .models import Education, Experience, Contact

# Create your views here.


context = {
    'educations': Education.objects.all(),
    'experiences': Experience.objects.all(),
    'contacts': Contact.objects.all(),
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


# _____________________________create_____________________________
def create_edu(request):
    if request.method == 'POST':
        level = request.POST['level']
        institute = request.POST['institute']
        bio = request.POST['bio']
        location = request.POST['location']
        date_from = request.POST['date_from']
        date_to = request.POST['date_to']

        obj = Education(level=level, institute=institute, bio=bio, location=location, date_from=date_from, date_to=date_to)
        obj.save()
        return redirect('crud:home')
    return render(request, 'crud/create_edu.html', context)


def create_experience(request):
    if request.method == 'POST':
        job_title = request.POST['job_title']
        subjects = request.POST['subjects']
        company = request.POST['company']
        date_from = request.POST['date_from']
        date_to = request.POST['date_to']

        obj = Experience(job_title=job_title, subjects=subjects, company=company, date_from=date_from, date_to=date_to)
        obj.save()
        return redirect('crud:home')
    return render(request, 'crud/create_experience.html', context)


def create_contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']

        obj = Contact(email=email, phone=phone, address=address)
        obj.save()
        return redirect('crud:home')
    return render(request, 'crud/create_contact.html', context)
