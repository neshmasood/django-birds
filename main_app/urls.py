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
    path('birds/<int:pk>/delete', views.Bird_Delete.as_view(), name="bird_delete"),
    path('user/<username>/', views.profile, name='profile'),
    path('birdhouses/', views.birdhouses_index, name='birdhouses_index'),
    path('birdhouses/<int:birdhouse_id>', views.birdhouses_show, name='birdhouses_show'),
    path('birdhouses/create/', views.BirdHouseCreate.as_view(), name='birdhouses_create'),
    path('birdhouses/<int:pk>/update/', views.BirdHouseUpdate.as_view(), name='birdhouses_update'),
    path('birdhouses/<int:pk>/delete/', views.BirdHouseDelete.as_view(), name='birdhouses_delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup')
]