from dataclasses import fields
from rest_framework import serializers
from web_app.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
#        fields('first_name','last_name')
        fields="__all__"