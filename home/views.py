from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage


def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def blog(request):
    return render(request, 'home/blog.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save message to the database
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact_success')  # Redirect to success page
        else:
            messages.error(request, "There was an error. Please try again.")

    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'home/contact_success.html')

def faq(request):
    return render(request, 'home/faq.html')

#Footer
def help(request):
    return render(request, 'home/help.html', {'timestamp': now().timestamp()})

def privacy(request):
    return render(request, 'home/privacy.html')

def terms(request):
    return render(request, 'home/terms.html')