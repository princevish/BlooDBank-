from django.urls import path
from .import views

urlpatterns = [

    path('', views.home, name="home"),
    path('blood', views.blood, name="blood"),
    path('about', views.about, name="about"),
    path('event', views.eventblog, name="event"),
    
    path('bloodbank', views.bloodbank1, name="bloodbank1"),
    path('changeavailable', views.changeavailable, name="changeavailable"),
    path('<int:ProfileModel_id>', views.report, name='report'),
]