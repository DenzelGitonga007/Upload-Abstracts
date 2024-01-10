from django.urls import path
from .import views

app_name = "accounts"

urlpatterns = [
    path('register/', views.register, name="register"), # Register url
    path('login/', views.user_login, name="login"), # Login url
    path('', views.home, name='home'), # Landing page
    path('logout/', views.user_logout, name="logout") # Logout user
    
]