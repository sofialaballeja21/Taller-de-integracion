from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('signup/', views.signup, name='signup'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('eliminar-cuenta/', views.eliminar_usuario, name='eliminar_usuario'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    


    # Rutas de autenticación (login/logout)
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]