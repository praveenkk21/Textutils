import django.shortcuts
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StudentSub
from .models import Student
from .serializers import StudentSerializer, StudentSubSerializer

@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class student_sub_details(APIView):
    def get(self,request):
        students = StudentSub.objects.all()
        serializer = StudentSubSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        sid = request.data.get('sid')
        serializer = StudentSubSerializer(data=request.data)
        # Check if student exists
        if not Student.objects.filter(id=sid).exists():
            return Response({'error': 'Student with given ID does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            
        elif serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
# @api_view(['GET', 'POST'])
# def student_sub_details(request):
#     if request.method == 'GET':
#         students = StudentSub.objects.all()
#         serializer = StudentSubSerializer(students, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         sid = request.data.get('sid')
#         serializer = StudentSubSerializer(data=request.data)
#         # Check if student exists
#         if not Student.objects.filter(id=sid).exists():
#             return Response({'error': 'Student with given ID does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            
#         elif serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)