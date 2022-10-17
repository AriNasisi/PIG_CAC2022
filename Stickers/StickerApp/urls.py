from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('item/<str:id>', views.individual),
    

]
