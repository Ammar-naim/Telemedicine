from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
	path('registerDoctor', registerDoctor, name='registerDoctor'),
	path('registerPharma', registerPharma, name='registerPharma'),
    path('registerUser', registerUser, name='registerUser'),
    path('loginUser', loginUser, name='loginUser'),
    path('loginDoctor', loginDoctor, name='loginDoctor'),
    path('loginPharma', loginPharma, name='loginPharma'),
	
]
