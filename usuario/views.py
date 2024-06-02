from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class ValidarTokenView(APIView):
    def post(self, request):
        token_data = request.data.get('token')
        token = Token.objects.filter(key=token_data).first()

        if token:
            user = token.user
            empresas = user.user_empresa.all()
            empresa = empresas[0].empresa


            return Response({'planes':empresa.planes}, status=200)

        return Response({'valido': False}, status=400)

class AuthView(APIView):
    def post(self, request):
        user_data = request.data.get('user')
        password_data = request.data.get('password')

        user = authenticate(username=user_data, password=password_data)

        if user:
            token, created = Token.objects.get_or_create(user=user)

            empresas = user.user_empresa.all()
            empresa = None
            
            if empresas.exists():
                empresa = empresas[0].empresa.nombre
                tipo = empresas[0].empresa.get_tipo_display()

            return Response({'user': user.username, 
                             'token': token.key, 
                             'empresa': empresa,
                             'tipo': tipo
                             }, status=200)

        return Response({'error': 'Usuario o contraseña incorrectos'}, status=400)