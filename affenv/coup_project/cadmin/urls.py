from django.urls import path, include
import cadmin.views

urlpatterns = [
    path('', cadmin.views.product)
]
