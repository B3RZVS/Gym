from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class ValidarTokenView(APIView):
    def post(self, request):
        token_data = request.data.get('token')
        token = Token.objects.filter(key=token_data).first()

        if token:
            user = token.user
            role = user.role.name

            return Response({'role': role}, status=200)

        return Response({'valido': False}, status=400)

class AuthView(APIView):
    def post(self, request):
        user_data = request.data.get('username')
        password_data = request.data.get('password')

        user = authenticate(username=user_data, password=password_data)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            role = user.role.name if user.role else None

            return Response({
                'user': user.username,
                'token': token.key,
                'role': role
            }, status=200)

        return Response({'error': 'Usuario o contraseña incorrectos'}, status=400)
