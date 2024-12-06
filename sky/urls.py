from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("testimonial",views.testimonial,name="testimonial"),
    path("property-type",views.propertytype,name="property-type"),
    path("404",views.a404,name="404"),
    path("property-agent",views.propertyagent,name="property-agent"),
    path("property-list",views.propertylist,name="property-list"),
]