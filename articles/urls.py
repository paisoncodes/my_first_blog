from django.urls import path
from . import views


app_name = 'blog'


urlpatterns = [
    path('<slug>/delete/', views.delete_blog_view, name='delete'),
    path('create/', views.create_blog_view, name='create'),
    path('<slug>/', views.detail_blog_view, name='detail'),
    path('<slug>/edit', views.edit_blog_view, name='edit')
]
