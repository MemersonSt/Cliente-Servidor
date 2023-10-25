from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ('id', 'username', 'email', 'password', 'is_staff')#forma de mostrar los datos 1
        fields = '__all__'#forma de mostrar los datos 2

    