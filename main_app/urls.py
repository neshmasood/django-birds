from django.urls import path
from . import views

#this is like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),  #<- here we have added the new path
    path('about/', views.About.as_view(), name="about"),
    path('birds/', views.Bird_List.as_view(), name="bird_list"),
]