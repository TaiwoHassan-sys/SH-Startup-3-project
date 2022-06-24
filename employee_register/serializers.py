from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Employee , Vacation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "fullname", "emp_code", "mobile", "vac_request"]
