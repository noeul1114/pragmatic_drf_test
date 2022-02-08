from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView

from accountapp.models import PragmaticUser
from accountapp.serializers import PragmaticUserSerializer


def hello_world(request):
    return HttpResponse("HELLO WORLD!")


class AccountCreateAPIView(CreateAPIView):
    queryset = PragmaticUser
    serializer_class = PragmaticUserSerializer

    permission_classes = [permissions.AllowAny]
    authentication_classes = [TokenAuthentication]
