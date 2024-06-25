from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('',views.index, name='index'),
    path('create/',views.post_create, name='post_create'),
    # path('create/',views.post, name='post_create'),
]