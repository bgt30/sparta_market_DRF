from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignUpView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('<str:username>/', views.ProfileView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('password/', views.PasswordChangeView.as_view()),
    path('delete/', views.AccountDeleteView.as_view()),
    path('<str:username>/follow/', views.FollowView.as_view()),
] 