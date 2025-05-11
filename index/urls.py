from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('assistance', views.request_assistance, name='assistance'),
    path('join', views.request_to_join, name='join'),
    path('submit_membership_request', views.submit_membership_request, name='submit_membership_request'),
    path('submit-assistance-request', views.submit_assistance_request, name='submit_assistance_request'),
]