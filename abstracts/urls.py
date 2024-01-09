from django.urls import path
from . import views
app_name = "abstracts"

urlpatterns = [
    path('upload/', views.abstract_create, name="upload"), # Upload abstract
]