from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signUp, name='signup'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('watch/', views.watch, name='watch'),
    path('recommend/', views.recommend, name='recommend'),
    path('Action/',views.Action,name='Action'),
    path('Adventure/', views.Adventure, name='Adventure'),
    path('Animation/', views.Animation, name='Animation'),
    path('Biography/', views.Biography, name='Biography'),
    path('Comedy/', views.Comedy, name='Comedy'),
    path('Crime/', views.Crime, name='Crime'),
    path('Drama/', views.Drama, name='Drama'),
    path('Fantasy/', views.Fantasy, name='Fantasy'),
    path('History/', views.History, name='History'),
    path('Mystery/', views.Mystery, name='Mystery'),
    path('Sci-Fi/', views.SciFi, name='Sci-Fi'),
    path('Romance/', views.Romance, name='Romance'),
    path('Thriller/', views.Thriller, name='Thriller'),
    path('Sports/', views.Sports, name='Sports'),

]