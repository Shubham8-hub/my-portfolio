from django.urls import path
from . import views

# app_name = "main"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("about", views.about, name="about"),
    path("resume", views.resume, name="resume"),
    path("projects", views.projects, name="projects"),
    # path("blog", views.blog, name="blog"),
    path("contact", views.contact, name="contact"),
    path("saveEnquiry", views.saveEnquiry, name="saveEnquiry"),
]