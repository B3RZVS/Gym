from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Usuario

class ValidarTokenView(APIView):
    def post(self, request):
        token_data = request.data.get('token')
        token = Token.objects.filter(key=token_data).first()

        if token:
            user = token.user
             
            return Response({'user': user.username}, status=200)

        return Response({'valido': False}, status=400)

class AuthView(APIView):
    def post(self, request):
        user_data = request.data.get('username')
        password_data = request.data.get('password')

        user = authenticate(username=user_data, password=password_data)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'user': user.username,
                'token': token.key,
                'password': user.password
            }, status=200)

        return Response({'error': 'Usuario o contraseña incorrectos'}, status=400)

class Register(APIView):
    def post(self,request):
        data= request.data
        campos=["username","password","nombre","apellido","email","telefono"]
        try:
            Usuario.comprobacionCampos(campos, request)
        except ValidationError as e:
            return Response(e.detail, status=400)
        
        
        if User.objects.filter(username=data['username']).exists():
            return Response({"error":f"El nombre de usuario '{data['username']}' ya existe"},status=400)
        
        user = User.objects.create_user(username=data['username'], password=data['password'])

        token = Token.objects.create(user=user)

        usuario = Usuario.objects.create(
            user=user,
            nombre= data['nombre'],
            apellido=data['apellido'],
            email=data['email'],
            telefono=data['telefono']
        )

        return Response({"mensaje":f"Usuario creado exitosamente", 
                         "usuario": {user.username}, 
                          "token":{token.key}} ,status=200)
            
            