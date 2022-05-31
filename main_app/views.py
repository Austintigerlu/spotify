from django.views.generic.base import TemplateView

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"
