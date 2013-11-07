from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from rest_framework.generics import (
		ListCreateAPIView
	)

from board.models import Dealer


class UserViewSet(viewsets.ModelViewSet):
    model = User
    fields = ('username','lastlogin')


class GroupViewSet(viewsets.ModelViewSet):
    model = Group


class DealerViewSet(viewsets.ModelViewSet):
	model = Dealer