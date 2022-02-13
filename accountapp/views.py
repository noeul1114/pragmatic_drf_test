from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from accountapp.models import PragmaticUser
from accountapp.permissions import AccountPermission
from accountapp.serializers import PragmaticUserSerializer, PragmaticUserSerializerWithoutEmail


def hello_world(request):
    return HttpResponse("HELLO WORLD!")


class LoginApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        user = authenticate(email=request.POST.get('email'),
                            password=request.POST.get('password'),)
        if user is not None:
            token = Token.objects.get(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid username or password'},
                            headers={'WWW-Authenticate': self.get_authenticate_header(request)},
                            status=status.HTTP_401_UNAUTHORIZED)


class PragmaticUserAPIViewSet(ModelViewSet):
    queryset = PragmaticUser.objects.all()
    serializer_class = PragmaticUserSerializer

    permission_classes = [AccountPermission]

    http_method_names = ['get', 'post', 'patch', 'delete', 'options', 'head']

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PragmaticUserSerializerWithoutEmail
        else:
            return PragmaticUserSerializer

