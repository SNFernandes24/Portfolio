from django.shortcuts import render, redirect
from .models import Job
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template

# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(name, email, message)

        subject = 'Contact Form Recieved'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = ['snfernandes24@gmail.com']

        context = {
            'user': name,
            'email': email,
            'message': message
        }

        contact_message = get_template('contact_message.txt').render(context)

        send_mail(subject, contact_message, from_email, to_email, fail_silently = True)

        return redirect("/")
    return render(request, "jobs/home.html", {})
