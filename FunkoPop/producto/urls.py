from django.urls import path
from producto import views

urlpatterns = [
    path('index_productos', views.index, name='index_productos'),
    path('producto_rest/', views.productos_rest, name='productos_rest'),
    path('add_producto/', views.add_producto_view, name='add_producto'),
    path('new_producto/', views.NewProductoView.as_view(), name='new_producto'),
]