from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View # View class to handle requests
from django.http import HttpResponse, HttpResponseRedirect #This is our responses
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Bird
from django.contrib.auth.models import User


# Create your views here.

class Home(TemplateView): 
    template_name = 'home.html'

    # OLD GET REQUEST
    # Here we are adding a method that will be ran when we are dealing with a GET request
    # def get(self, request):
    #     # Here we are returning a generic response
    #     # This is similar to res.send() in express
    #     return HttpResponse("Birds Home")

class About(TemplateView):
    template_name = 'about.html'
    # OLD GET REQ
    # def get(self, request):
    #     return HttpResponse("Birds About")


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
            context['header'] = "Beautiful Birds" # this is where we add the key into our context object for the view to use
        return context

class Bird_Create(CreateView):
    model = Bird
    fields = ['name', 'img', 'age', 'gender', 'user']
    template_name = "bird_create.html"
    # success_url = "/birds/"
    # def get_success_url(self):
    #     return reverse('bird_detail', kwargs={'pk': self.object.pk})
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/birds')


class Bird_Detail(DetailView): 
    model = Bird
    template_name="bird_detail.html"


class Bird_Update(UpdateView):
    model = Bird
    fields = ['name', 'img', 'age', 'gender']
    template_name = "bird_update.html"
    # success_url = "/birds/"
    def get_success_url(self):
        return reverse('bird_detail', kwargs={'pk': self.object.pk})


class Bird_Delete(DeleteView):
    model = Bird
    template_name = "bird_delete_confirm.html"
    success_url = "/birds/"


def profile(request, username):
    user = User.objects.get(username=username)
    birds = Bird.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'birds': birds})

