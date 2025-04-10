from django.shortcuts import render
from .models import*
from .serializers import*
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def todo_api(request):
    if request.method == 'POST':
        x=ToDoSerializer(data=request.data)
        if x.is_valid():
            x.save()
            return Response({'message':"Data Post Successfully", 'response_code':200})
        return Response({'message':x.errors, 'response_code':400})
    if request.method == 'GET':
        todo= ToDo.objects.all()
        x = ToDoSerializer(todo, many=True)
        return Response({'message':"Data Get Successfully", 'response_code':200, 'data':x.data})
    if request.method == 'PATCH':
        todo_id= request.data.get('todo_id')
        if todo_id:
            if not ToDo.objects.filter(id=todo_id).exists():
                return Response({"message": "This id does not exist", "response_code":400})
            todo= ToDo.objects.get(id=todo_id)
            x= ToDoSerializer(todo, data=request.data, partial=True)
            if x.is_valid():
                x.save()
                return Response({"message": "Data Update Successfully", "response_code": 200})
            return Response(x.errors, status=400)
        return Response({"message": "todo id not found", "response_code":400})
    if request.method == 'DELETE':
        todo_id= request.data.get('todo_id')
        if todo_id:
            if not ToDo.objects.filter(id=todo_id).exists():
                return Response({"message": "This id does not exist", "response_code":400})
            todo= ToDo.objects.get(id=todo_id).delete()
            return Response({"message": "Data Deleted Successfully", "response_code": 200})
        return Response({"message": "Student id not found", "response_code":400})


