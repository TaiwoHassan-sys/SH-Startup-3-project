from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Employee , Vacation


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class VacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = ["id", "vac_request"]

class EmployeeSerializer(serializers.ModelSerializer):
    # vac_request = VacationSerializer()
    
    class Meta:
        model = Employee
        fields = ["id", "fullname", "emp_code", "mobile", "vac_request"]




