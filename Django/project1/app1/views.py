from django.shortcuts import render, redirect
from .forms import ContactForm
from .forms import PracticeForm
from .models import Practice
from .models import Contact
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page after saving
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
def success_view(request):
    return render(request, 'success.html')

def practice_view(request):
    if request.method == 'POST':
        form = PracticeForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to a success page after saving
    else:
        form = PracticeForm()

    return render(request, 'practice.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Check if a user with this username and password exists
            user = Practice.objects.filter(username=username, password=password).first()

            if user:
                # If user exists, send success message
                messages.success(request, f'Welcome {username}!')
            else:
                # If no such user, send error message
                messages.error(request, 'No record found. Please check your credentials.')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
def login_list(request):
    practices = Practice.objects.all()  # Query all Practice records
    return render(request, 'login_list.html', {'practices': practices})
def contact_list(request):
    contacts = Contact.objects.all()  # Query all Practice records
    return render(request, 'contact_list.html', {'contacts': contacts})