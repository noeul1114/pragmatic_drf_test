from django.urls import path

from accountapp.views import hello_world, AccountCreateAPIView

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('', AccountCreateAPIView.as_view(), name='create'),

]
