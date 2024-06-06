from django.urls import path
from . import views

urlpatterns = [
    path("address-form/", views.address_form, name="address_form"),
    path("load-cities/", views.load_cities, name="load_cities"),
    # سایر URL‌های home اینجا اضافه شوند
]
