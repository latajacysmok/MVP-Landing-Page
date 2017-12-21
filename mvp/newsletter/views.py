from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm, SignUpForm
from .models import SignUp

def home(request):
    title = "Sign Up Now"
    # if request.user.is_authenticated():
    #     title = "My title {}".format(request.user)

    form = SignUpForm(request.POST)

    context = {
        "title": title,
        "form": form,
    }

    if form.is_valid():
         form.save()
         # instance = form.save(commit=False)
         # instance.save()
         context = {
            "title": "Thank you"
         }
    # if request.user.is_authenticated() and request.user.is_staff:
    #     queryset = SignUp.objects.all().order_by('-timestamp')
    #     context = {
    #         "queryset": queryset
    #     }

    return render(request, "home.html", context)

def contact(request):
    title='Contact'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key in form.cleaned_data:
        #     print(key + ":")
        #     print(form.cleaned_data.get(key))
        form_full_name = form.cleaned_data.get("full_name")
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        subject = 'Site contact from'
        contact_message = "%s = %s via %s"%(
            form_full_name,
            form_message,
            form_email)
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'yourotheremail@gmail.com']
        send_mail(subject,
                  contact_message,
                  from_email,
                  [to_email],
                  fail_silently=True)
    context = {
        "form": form,
        "title": title,

    }
    return render(request, "forms.html", context)

def about(request):
    title='About'
    return render(request, "about.html", {})