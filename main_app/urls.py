from django.urls import path
from . import views

#this is like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),  #<- here we have added the new path
    path('about/', views.About.as_view(), name="about"),
    path('birds/', views.Bird_List.as_view(), name="bird_list"),
    path('birds/new/', views.Bird_Create.as_view(), name="bird_create"),

    path('birds/<int:pk>/', views.Bird_Detail.as_view(), name="bird_detail"),
    path('birds/<int:pk>/update', views.Bird_Update.as_view(), name="bird_update"),
    path('birds/<int:pk>/delete', views.Bird_Delete.as_view(), name="bird_delete")
   
]