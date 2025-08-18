from django.urls import path
from . import views
from django.contrib.auth.urls import views as auth_views

urlpatterns = [
    path('home/',views.myhome),
    path('post/',views.post_list,name = 'post_list'),
    path('create/',views.post_create,name = 'post_create'),
    path('<int:post_id>/edit/',views.post_edit,name = 'post_edit'),
    path('<int:post_id>/delete/',views.post_delete,name = 'post_delete'),
    path('register/',views.register, name = 'register'),
    path('login/',views.login, name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]

