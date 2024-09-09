from django.contrib import admin
from django.urls import path
from app.views import index, contact_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="home"),
    path("contact/", contact_form, name="contact_form"),
]
