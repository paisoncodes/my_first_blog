from django.urls import path

from account import views


urlpatterns = [
    path('account/', views.account_view, name='account'),
    path('login/', views.login_view, name='login'),
    path("logout/", views.logout_request, name= "logout"),
    path('register/', views.registration_view, name='register'),
    path('authenticate/', views.must_authenticate_view, name='must_authenticate')
]