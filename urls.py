from django.urls import path
from . import views 

urlpatterns  = [
    path('', views.home),
    path('registarcompra/', views.registarcompra),
    path('eliminacionCelular/<int:id>', views.eliminar_celulares ),
    path('edicionCelular/<id>', views.edicionCelular , name='editarCelular'  ),
    path('editarCompra/',views.editarcompra),
    ]
