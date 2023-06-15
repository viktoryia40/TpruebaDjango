from rest_framework import serializers
from mascotarApp.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    longitud_nombre = serializers.SerializerMethodField()
    
    class Meta:
        model = Producto
        fields = "__all__"
        
    def get_longitud_nombre(self, object):
        cantidad_caracteres = len(object.nombre)
        return cantidad_caracteres
        
    def validate(self, data):
        if data['nombre'] == data ['descripcion']:
            raise serializers.ValidationError("El nombre y la direccion deben ser diferentes")
        else:
            return data

# def column_longitud(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("El valor es demasiado corto")

# class ProductoSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     nombre = serializers.CharField(validators=[column_longitud])
#     precio = serializers.DecimalField(max_digits=8, decimal_places=2)
#     descripcion = serializers.CharField(validators=[column_longitud])
#     linkImagen = serializers.URLField()
    
#     def create(self, validated_data):
#         return Producto.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.nombre = validated_data.get('nombre', instance.nombre)
#         instance.precio = validated_data.get('precio', instance.precio)
#         instance.descripcion = validated_data.get('descripcion', instance.descripcion)
#         instance.linkImagen = validated_data.get('linkImagen', instance.linkImagen)
#         isinstance.save()
#         return instance
        
#     def validate(self, data):
#         if data['nombre'] == data ['descripcion']:
#             raise serializers.ValidationError("El nombre y la direccion deben ser diferentes")
#         else:
#             return data
        
