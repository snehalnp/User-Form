from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms.user_form import UserFormForm
from .models import UserForm
from datetime import datetime


# Create your views here.


def user_form_view(request):
    if request.method == 'POST':
        form = UserFormForm(request.POST)
        if form.is_valid():
            form.save()
            send_email_notification(form.cleaned_data['email'])
            return redirect('submitted_forms')
    else:
        form = UserFormForm()
    return render(request, 'user_form.html', {'form': form})

def submitted_forms_view(request):
    submitted_forms = UserForm.objects.all()
    return render(request, 'submitted_forms.html', {'submitted_forms':submitted_forms})

def send_email_notification(email):
    subject = "Successful Submission"
    current_datetime = datetime.now().time()
    message = f"Your user form has been submitted successfully on {current_datetime}"
    # from_email = 'snpalve20@gmail.com'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

