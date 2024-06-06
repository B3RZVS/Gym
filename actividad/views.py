from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Actividad, Ejercicio, Serie
# Create your views here.

class ActividadAbm(APIView):
    
    def get(self, request):
        actividades= Actividad.objects.filter(activo=True)
        data=[]
        for actividad in actividades:
            data.append({
                "ejercicio": actividad.ejercicio,
                "tiempo descanso": actividad.tiempoDescanso
            })
        
        return Response({"actividades":data})
    
    def post(self, request):

        data= request.data
        campos=['ejercicio', 'tiempoDescanso']
        try:
            Actividad.comprobacionCampos(campos, request)
        except ValidationError as e:
            return Response(e.detail, status=400)
        
        try: 
            ejercicio= Ejercicio.objects.get(id=data['ejercicio'])
        except Ejercicio.DoesNotExist:
            return Response({"error":"El ejercicio no existe"},status=404)
        
        actividad= Actividad.objects.create(ejercicio=ejercicio, tiempoDescanso=data['tiempoDescanso'])

        return Response({"mensaje":"actividad creada con exito", 
                         "id": actividad.id}, status=200)
     
    def put(self, request):

        if not 'id' in request.data:
            return Response({"error":"Falta el id de la actividad"},status=400)
        id=request.data['id']
        try:
            actividad= Actividad.objects.get(id=id)
        except Actividad.DoesNotExist:
            return Response({"error":"la actividad no existe"}, status=404)
        
        if 'tiempoDescanso' in request.data:
            actividad.tiempoDescanso= request.data['tiempoDescanso']
            actividad.save()

    def delete(self,request):

        if not 'id' in request.data:
            return Response({"error":"Falta el id de la actividad"},status=400)
        
        id=request.data['id']
        try:
            actividad= Actividad.objects.get(id=id)
        except Actividad.DoesNotExist:
            return Response({"error":"la actividad no existe"}, status=404)
        
        actividad.cambioEstado()
        return Response({"mensaje":"actividad borrada", "estado":actividad.activo},status=200)
    
class SerieAbm(APIView):

    def get(self, request):

        series= Serie.objects.filter(activo=True)
        data=[]
        for serie in series:
            data.append({
                "repeticion": serie.repeticion,
                "peso": serie.peso,
                "tiempo": serie.tiempo,
                "secuencia": serie.secuencia,
                "actividad": serie.actividad
            })
        
        return Response({"actividades":data})
    
    def post(self, request):

        data= request.data
        campos=['repeticion','peso','tiempo','secuencia', 'actividad']

        try:
            Actividad.comprobacionCampos(campos, request)
        except ValidationError as e:
            return Response(e.detail, status=400)
        
        try:
            actividad= Actividad.objects.get(id=data['actividad'])
        except Actividad.DoesNotExist:
            return Response({"error":"La actividad no existe"},status=404)
        
        serie= Serie.objects.create(
            repeticion=data['repeticion'],
            peso= data['peso'],
            tiempo=data['tiempo'],
            secuencia=data['secuencia'],
            actividad=data['actividad'])
        
        return Response ({"mensaje":"Serie creada exitosamente","id":serie.id}, status=200)
    
    def put(self,request):

        if not 'id' in request.data:
            return Response({"error":"Falta el id de la actividad"},status=400)
        id=request.data['id']

        try:
            serie= Serie.objects.get(id=id)
        except Serie.DoesNotExist:
            return Response({"error":"La serie no existe"}, status=404)
        
        for i, value in request.data.items():

            if i != 'id':
                setattr(serie, i, value)
        serie.save()
        return Response({"Mensaje":"Serie modificada con exito", "serie":serie},status=200)
    
    def delete(self,request):

        if not 'id' in request.data:
            return Response({"error":"Falta el id de la actividad"},status=400)
        
        id=request.data['id']
        try:
            serie= Serie.objects.get(id=id)
        except Actividad.DoesNotExist:
            return Response({"error":"la serie no existe"}, status=404)
        
        serie.cambioEstado()
        return Response({"mensaje":"actividad borrada", "estado":serie.activo},status=200)
    