from django.urls import path

from accounts import views


urlpatterns = [
    path('login/', views.LogInView.as_view(), name='login'),
    path('signin/', views.SignInView.as_view(), name='signin'),
]
