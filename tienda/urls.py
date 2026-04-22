from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('producto/', views.producto, name='producto'),
    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('producto/<int:id>/', views.detalle_producto, name='detalle_producto'),  
    path('carrito/agregar/<int:id>/', views.agregar_carrito, name='agregar_carrito'),  
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/eliminar/<int:id>/', views.eliminar_del_carrito, name='eliminar_carrito')
]