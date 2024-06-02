from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from models import Categoria, Musculo, Ejercicio, EjercicioMusculo

class CategoriaAbm(APIView):
    def get(self,request):
        categorias= Categoria.objects.filter(activo=True)
        data=[]
        for categoria in categorias:
            data.append({
                "nombre": categoria.nombre
            })
        return Response({"categorias": data})
    
    def post(self,request):
        
        if not 'nombre' in request.data:
            return Response({"error: Falta el campo nombre"},status=400)
        
        nombre= request.data['nombre']
        
        try:
            aux= Categoria.objects.filter(nombre= nombre, activo=True)

        except Categoria.DoesNotExist:
            categoria= Categoria(nombre= nombre)
            categoria.save()
            return Response({"mensaje":"Categoria creada con exito",
                             "id": categoria.id}, status= 200)
        
        return Response({"error":"La categoria ya existe"})
    
    def delete(self, request):
        data= request.data
        try:
            id= data.get("id")
            categoria = Categoria.objects.get(id=id)

        except Categoria.DoesNotExist:
            return Response({"error": f"La categoria '{id}' no existe"}, status=404)

        categoria.cambioEstado()

        return Response({"mensaje": "Categoria eliminado exitosamente"}, status=200)    
            
class MusculoAbm(APIView):
    def get(self, request):
        musculos= Musculo.objects.all()
        data=[]
        for musculo in musculos:
            data.append({
                "nombre": musculo.nombre
            })          
        return Response({"musculos":data})

    def post(self,request):

        if not 'nombre' in request.data:
            return Response({"error":"falta el campo nombre"},status=400)

        nombre = request.data['nombre']
        
        try: 
            aux= Musculo.objects.get(nombre=nombre)
        except Musculo.DoesNotExist:
            musculo= Musculo(nombre=nombre)
            musculo.save
            return Response({"mensaje":"musculo creado con exito",
                            "id": musculo.id}, status=200)
        
        return Response({"error":"La categoria ya existe"})

    def delete(self, request):
        if not 'id' in request.data:
            return Response({"error":"falta el id del musculo"},status=400)
        
        try:
            id= request.data.get('id')
            musculo= Musculo.objects.get(id=id)

        except Musculo.DoesNotExist:

            return Response({"error":" el musculo no existe"},status=404)
        
        musculo.cambioEstado()

            
class EjercicioAbm(APIView):
    def get(self, request):
        ejercicios= Ejercicio.objects.filter(activo=True)
        data=[]

        for ejercicio in ejercicios:
            data.append({
                "nombre": ejercicio.nombre,
                "descripcion": ejercicio.descripcion,
                #Agregar la imagen,
                "categoria": ejercicio.categoria.nombre
            })
        return Response({"ejercicios":data}) 
    
    def put(self, request):

        data= request.data

        if not 'id' in request.data:
            return Response({"error":"falta el id del ejercicio"},status=400)
        
        try:
            ejercicio= Ejercicio.objects.get(id=request.data.get('id'), activo=True)
            
        except Ejercicio.DoesNotExist:
            return Response({"error":"El ejercicio no exixte"}, status=404)
        
        #buscamos el ejercicio musculo y le cambio los musculos
        if 'musculos' in data:
            detalles= ejercicio.detalles.all() # Todos los objetos detalles del ejercicio
            detalles.delete()
            musculos= data.get('musculos') #lista de los ID pasados
        
            for musculo_id in musculos: #recorro los id de los musculos pasados
                try:
                    musculo= Musculo.objects.get(id=musculo_id)
                    new_detalle= EjercicioMusculo(ejercicio=ejercicio, musculo=musculo)
                    new_detalle.save()

                except Musculo.DoesNotExist:

                    return Response({"error": f"El musculo {musculo_id} no existe"}, status=404)
                             
        #Actualizamos los campos que se comprenden en el cuerpo de la request
    
        for i, value in data.items():

            if i != 'id':
                setattr(ejercicio, i, value)
        ejercicio.save()
        return Response({"mensaje": "Ejercicio actualizado exitosamente"}, status=200)
    
    def delete(self, request):
        if not 'id' in request.data:
            return Response({"error":"falta el id del ejercicio"},status=400)
        
        try:
            id= request.data.get('id')
            ejercicio= Ejercicio.objects.get(id=id)

        except Ejercicio.DoesNotExist:

            return Response({"error":" el ejercicio no existe"},status=404)
        
        ejercicio.cambioEstado()

#agregar post