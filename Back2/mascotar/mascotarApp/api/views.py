from rest_framework.response import Response
from mascotarApp.models import Producto
from mascotarApp.api.serializers import ProductoSerializer
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

class ProductoListAV(APIView):
    
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
class ProductoDetalleAV(APIView):
    def get(self, request, pk):
        try:
            producto = Producto.objects.get(pk = pk)
        except Producto.DoesNotExist:
            return Response({'error': 'El producto no encontrado'}, status = status.HTTP_404_NOT_FOUND)
        
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            producto = Producto.objects.get(pk = pk)
        except Producto.DoesNotExist:
            return Response({'error': 'El producto no encontrado'}, status = status.HTTP_404_NOT_FOUND)
        
        serializer = ProductoSerializer(producto, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            producto = Producto.objects.get(pk = pk)
        except Producto.DoesNotExist:
            return Response({'error': 'El producto no encontrado'}, status = status.HTTP_404_NOT_FOUND)
        
        producto.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
        
# @api_view(['GET', 'POST'])
# def producto_list(request):
#     if request.method == 'GET':
#         productos = Producto.objects.all()
#         serializer = ProductoSerializer(productos, many = True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         de_serializer = ProductoSerializer(data = request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors)
        
# @api_view(['GET', 'PUT', 'DELETE'])
# def producto_detalle(request, pk):
#     if request.method == 'GET':
#         try:
#             producto = Producto.objects.get(pk=pk)
#             serializer = ProductoSerializer(producto)
#             return Response(serializer.data)
#         except Producto.DoesNotExist:
#             return Response({'Error': 'El producto no existe'}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'PUT':
#         producto = Producto.objects.get(pk=pk)
#         de_serializer = ProductoSerializer(producto, data = request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
#     if request.method == 'DELETE':
#         try:
#             producto = Producto.objects.get(pk=pk)
#             producto.delete()
#         except Producto.DoesNotExist:
#             return Response({'Error': 'El producto no existe'}, status=status.HTTP_404_NOT_FOUND)
         
#         return Response(status=status.HTTP_204_NO_CONTENT)
        