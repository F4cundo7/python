from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.form, name = 'login'),
    path('', views.index, name= 'home'),
    path('tasks/', views.task, name = 'Obras'),
    path('tasks/search/', views.tasks_search, name='tasks_search'),
    path('crear/', views.crear_obra, name = 'Crear Obra'),
    path('logout/', views.signout, name = 'logout'),
    path('signin/', views.signin, name = 'signin')
]
