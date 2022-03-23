from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View # View class to handle requests
from django.http import HttpResponse #This is our responses
from .models import Bird

# Create your views here.

class Home(TemplateView): 
    template_name = 'home.html'

    # OLD GET REQUEST
    # Here we are adding a method that will be ran when we are dealing with a GET request
    # def get(self, request):
    #     # Here we are returning a generic response
    #     # This is similar to res.send() in express
    #     return HttpResponse("Cats Home")

class About(TemplateView):
    template_name = 'about.html'
    # OLD GET REQ
    # def get(self, request):
    #     return HttpResponse("Birds About")


# ---------------------------------------------------
# ---------------------------------------------------
# after database, we no longer need class Bird

# class Bird: 

#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender


# birds = [
#     Bird("Cardi", 10, "Female"),
#     Bird("Robin", 2, "Male"),
#     Bird("Sparrow", 5, "Male"),
#     Bird("Woody", 1, "Male"),
#     Bird("Jay", 18, "Female")
# ]

# class Bird_List(TemplateView):
#     template_name = 'birdlist.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['birds'] = birds # this is where we add the key into our context object for the view to use
#         return context

# ---------------------------------------------------
# ---------------------------------------------------

class Bird_List(TemplateView):
    template_name = 'birdlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context['birds'] = Bird.objects.filter(name_icontains=name)
            context['header'] = f"Searching for {name}"
        else:
            context['birds'] = Bird.objects.all()
            context['header'] = "Birds" # this is where we add the key into our context object for the view to use
        return context