from rest_framework import serializers
from .models import StudentSub
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class StudentSubSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSub
        fields = '__all__'
