from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")
def testimonial(request):
    return render(request, "testimonial.html")
def propertytype(request):
    return render(request, "property-type.html")
def a404(request):
    return render(request, "404.html")
def propertyagent(request):
    return render(request, "property-agent.html")
def propertylist(request):
    return render(request, "property-list.html")



