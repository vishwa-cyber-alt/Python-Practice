from django import forms
from .models import Contact
from .models import Practice
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
class PracticeForm(forms.ModelForm):
    class Meta:
        model = Practice
        fields = ['username', 'password']
