from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View # View class to handle requests
from django.http import HttpResponse, HttpResponseRedirect #This is our responses
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Bird, BirdHouse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



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


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class Bird_Update(UpdateView):
    model = Bird
    fields = ['name', 'img', 'age', 'gender', 'birdhouses']
    template_name = "bird_update.html"
    # success_url = "/birds/"
    def get_success_url(self):
        return reverse('bird_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class Bird_Delete(DeleteView):
    model = Bird
    template_name = "bird_delete_confirm.html"
    success_url = "/birds/"


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    birds = Bird.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'birds': birds})


# BirdHouses view functions
def birdhouses_index(request):
    birdhouses = BirdHouse.objects.all()
    return render(request, 'birdhouse_index.html', {'birdhouses': birdhouses })

def birdhouses_show(request, birdhouse_id):
    birdhouse = BirdHouse.objects.get(id=birdhouse_id)
    return render(request, 'birdhouse_show.html', {'birdhouse': birdhouse})


@method_decorator(login_required, name='dispatch')
class BirdHouseCreate(CreateView):
    model = BirdHouse
    fields = '__all__'
    template_name = "birdhouse_form.html"
    success_url = '/birdhouses'


@method_decorator(login_required, name='dispatch')
class BirdHouseUpdate(UpdateView):
    model = BirdHouse
    fields = ['name', 'house_type']
    template_name = "birdhouse_update.html"
    success_url = '/birdhouses'


@method_decorator(login_required, name='dispatch')
class BirdHouseDelete(DeleteView):
    model = BirdHouse
    template_name = "birdhouse_confirm_delete.html"
    success_url = '/birdhouses'



# django auth
def login_view(request):
     # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')
    else: # it was a get request so send the empty login form
        # form = LoginForm()
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form}) 


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/birds')



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            HttpResponse('<h1>Try Again</h1>')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


