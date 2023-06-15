#from django.shortcuts import render
#from .models import Producto
#from django.http import JsonResponse

#def producto_list(request):
    #productos = Producto.objects.all()
    #data = {
        #'productos'#: list(productos.values())
    #}
    #return JsonResponse(data)

#def producto_detalle(request, pk):
    #productos = Producto.objects.get(pk=pk)
    #data = {
        #'nombre'#: productos.nombre,
        #'precio'#: productos.precio,
        #'descripcion'#: productos.descripcion,
        #'linkImagen'#: productos.linkImagen,
        
    #}
    #return JsonResponse(data)
