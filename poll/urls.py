from django.urls import path
from . import views
urlpatterns = [
   path('', views.show_poll),
   path('site/',views.add_poll),
]