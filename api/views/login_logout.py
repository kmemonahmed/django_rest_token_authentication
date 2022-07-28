from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from main.models import CustomUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Login Api
class LoginView(APIView):
    def post(self, request):
        user_login_key = request.data.get('user_login_key')
        password = request.data.get('password')
        print(user_login_key, password)
        
        try:
            user = CustomUser.objects.get(username =  user_login_key)
        except:
            try:
                user = CustomUser.objects.get(phone =  user_login_key)
            except:
                try:
                    user = CustomUser.objects.get(email =  user_login_key)
                except:
                    return Response({
                    'token': None,
                    'status': 400
                }, 400)

        if user.check_password(password) and user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            status = 200
            token_code = token.key
        else:
            token_code = None
            status = 400
        return Response({
            'token': token_code,
        }, status)

# Logout Api
class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        try:
            Token.objects.get(key = request.auth.key).delete()
            return Response({'message': 'Logout Succcessfully.', 'status' : 200}, 200)
        except Exception as e:
            return Response({'message': 'Logout Failed.', 'status' : 200}, 200)
