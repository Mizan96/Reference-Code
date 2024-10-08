# GenericAPI View and Model Mixin

from api.models import Student
from api.serializers import StudentSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class StdentViewSet(viewsets.ViewSet): 
    def list(self, request):
        print('**********LIST***********')
        print('Basename: ',self.basename)
        print('Action: ',self.action)
        print('Detail: ',self.detail)
        print('Suffix: ',self.suffix)
        print('Name: ',self.name)
        print('Description: ',self.description)
        print('**********End of List************')
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        print('**********Retrieve***********')
        print('Basename: ',self.basename)
        print('Action: ',self.action)
        print('Detail: ',self.detail)
        print('Suffix: ',self.suffix)
        print('Name: ',self.name)
        print('Description: ',self.description)
        print('**********End of Retrieve************')
        id=pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        
    def create(self, request):
        print('**********Create***********')
        print('Basename: ',self.basename)
        print('Action: ',self.action)
        print('Detail: ',self.detail)
        print('Suffix: ',self.suffix)
        print('Name: ',self.name)
        print('Description: ',self.description)
        print('**********End of Create************')
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk):
        print('**********Update***********')
        print('Basename: ',self.basename)
        print('Action: ',self.action)
        print('Detail: ',self.detail)
        print('Suffix: ',self.suffix)
        print('Name: ',self.name)
        print('Description: ',self.description)
        print('**********End of Update************')  
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        
    def partial_update(self, request, pk):
        print('**********Partial Update***********')
        print('Basename: ',self.basename)
        print('Action: ',self.action)
        print('Detail: ',self.detail)
        print('Suffix: ',self.suffix)
        print('Name: ',self.name)
        print('Description: ',self.description)
        print('**********End of Partial Update************')
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Partial Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    def destroy(self, request, pk): 
        print('**********Destroy***********')
        print('Basename: ',self.basename)
        print('Action: ',self.action)
        print('Detail: ',self.detail)
        print('Suffix: ',self.suffix)
        print('Name: ',self.name)
        print('Description: ',self.description)
        print('**********End of Destroy************')
        id = pk
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({'msg': 'Data Deleted'})
    

