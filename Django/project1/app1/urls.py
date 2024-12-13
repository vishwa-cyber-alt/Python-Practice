from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),  # For redirect after success
    path('practice/', views.practice_view, name='practice'),  # For redirect after success
    path('login_list/', views.login_list, name='employee_list'),
    path('contact_list/', views.contact_list, name='contact_list'),

]
