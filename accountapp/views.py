from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet

from accountapp.models import PragmaticUser
from accountapp.permissions import AccountPermission
from accountapp.serializers import PragmaticUserSerializer


def hello_world(request):
    return HttpResponse("HELLO WORLD!")


class PragmaticUserAPIViewSet(ModelViewSet):
    queryset = PragmaticUser.objects.all()
    serializer_class = PragmaticUserSerializer

    permission_classes = [AccountPermission]

