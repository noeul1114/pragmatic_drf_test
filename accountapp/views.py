from rest_framework import viewsets, status
from rest_framework.response import Response

from accountapp.models import PragmaticUser
from accountapp.serializers import PragmaticUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = PragmaticUser.objects.all()
    serializer_class = PragmaticUserSerializer

