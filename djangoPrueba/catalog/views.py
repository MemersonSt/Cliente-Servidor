from rest_framework import viewsets
from .serializer import UserSerializer
from .models import User

# Create your views here.
#Operaciones CRUD
#Create
#Read
#Update
#Delete

class UserViews(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()