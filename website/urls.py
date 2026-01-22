from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('schemes/', views.schemes, name='schemes'),
    path('contact/', views.contact, name='contact'),
]

