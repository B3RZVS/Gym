from django.forms import ValidationError
from rest_framework import status
from django.shortcuts import render
from requests import Response
from rest_framework.views import APIView
from .models import Plan, DiaPlan
from usuario.models import Usuario

# Create your views here.
class PlanAbm(APIView):
    
    def get(self, request):
        planes = Plan.objects.filter(activo=True)
        data=[]

        for plan in planes:
            data.append({
                'id': plan.id,
                'nombre': plan.nombre,
                'fecha Inicio': plan.fechaInicio,
                'creador': plan.creador,
            })

        return Response({"planes":data})    

    def post(self, request):

        campos= ('nombre', 'creador')
        data=request.data
        try:
            Plan.comprobacionCampos(campos, request)
        except ValidationError as e:
            return Response(e.detail, status= 400)
        
        try:
            usuario= Usuario.objects.get(id=data['id']) 
        except Usuario.DoesNotExist:
            return Response({"error":"El usuario no existe"}, status=404)
        
        if usuario.role == 1:
            plan= Plan.objects.create(
                nombre=data['nombre'],
                creador= usuario
            )
        else:
            return Response({"error": "el usuario no tiene el rol de profesor"}, status=400)
        
        return Response({"mensaje":"Plan creado exitosamente",
                         "id_plan":plan.id,
                         },status=200)
    
    #agregar el put

    def delete(self,request):
        if not 'id' in request.data:
            return Response({"error":"falta el id del plan"},status=400)
        
        try:
            plan= Plan.objects.get(id=request.data['id'])
        except Plan.DoesNotExist:
            return Response({"error":"el plan no existe"},status=404)
        
        plan.cambioEstado()
        return Response({"mensaje":"cambio de estado realizaco",
                         "activo":plan.activo})

class DiaPlanAbm(APIView):

    def get(self,request):
        diasPlan= DiaPlan.objects.filter(activo=True)
        data = list(map(lambda x: {'id':x.id, 'dia':x.dia,'plan': x.plan.nombre }, diasPlan))

        return Response({"dias":data})
    
    def post(self, request):

        campos= ('plan', 'dia', 'actividades')
        data=request.data
        try:
            DiaPlan.comprobacionCampos(campos, request)
        except ValidationError as e:
            return Response(e.detail, status= 400)
        
        try:
            plan= Plan.objects.get(id=data['plan'], activo=True)
        except Plan.DoesNotExist:
            return Response({"error":"El plan no existe"},status=404)
        
        if not DiaPlan.objects.filter(plan=plan, dia=data['dia']).exists():

            diaPlan= DiaPlan.objects.create(
                plan=plan,
                dia=data['dia']
            )

            try:
                actividades= diaPlan.asignarActividad(data['actividades'])
            except ValidationError as e:
                return Response(e.detail, status= 400)
            
            

            return Response({"mensaje":"Dia creado exitosamente",
                             "id":diaPlan.id,
                             'actividades': actividades}, status=200)
        else:
            return Response({"error":"El el plan ya tiene el dia creado"}, status=400)

    #agregar el put
    
    def delete(self,request):
        if not 'id' in request.data:
            return Response({"error":"falta el id del diaPlan"},status=400)
        
        try:
            diaPlan= DiaPlan.objects.get(id=request.data['id'])
        except Plan.DoesNotExist:
            return Response({"error":"el diaPlan no existe"},status=404)
        
        diaPlan.cambioEstado()
        return Response({"mensaje":"cambio de estado realizaco",
                         "activo":diaPlan.activo})
    
