from django.urls import path
from . import views
app_name = "abstracts"

urlpatterns = [
    path('upload/', views.abstract_create, name="upload"), # Upload abstract
    path('edit/<int:pk>/', views.abstract_edit, name="edit"), # Edit abstract
    path('delete/<int:pk>', views.abstract_delete, name="delete") # Delete abstract
]