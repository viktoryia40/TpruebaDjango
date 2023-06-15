from django.urls import path
#from mascotarApp.api.views import producto_list, producto_detalle
from mascotarApp.api.views import ProductoListAV, ProductoDetalleAV


urlpatterns = [
    path('list/', ProductoListAV.as_view(), name = 'producto-list'),
    path('<int:pk>', ProductoDetalleAV.as_view(), name= 'producto-detalle'),
]