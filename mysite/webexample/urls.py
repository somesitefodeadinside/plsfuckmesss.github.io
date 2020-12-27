from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='main_home'),
    path('about',views.about, name='main_about')
]