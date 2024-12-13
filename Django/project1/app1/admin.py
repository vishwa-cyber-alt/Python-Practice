# admin.py
from django.contrib import admin
from .models import Contact  # Import the model
from .models import Practice
# Register the model with the admin site
admin.site.register(Contact)
admin.site.register(Practice)

