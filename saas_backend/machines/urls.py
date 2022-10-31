from django.urls import path
from . import views

urlpatterns = [
    path('', views.machine_list),
    path('info/', views.machine_info),

]