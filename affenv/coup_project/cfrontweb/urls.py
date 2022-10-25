from django.urls import path, include
import cfrontweb.views

urlpatterns = [
    path('', cfrontweb.views.main)
]
