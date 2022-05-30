
from django.http import response
from .services.kernel_service import Kernel_Service
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(["GET"])
def initialize(request):
    if request.method == 'GET':
        kernel = Kernel_Service(0,'','start')
        response = [kernel.return_states()]
        return Response(response, status=status.HTTP_200_OK)

@api_view(["PUT"])
def kernel_operations_view(request):
    if request.method == 'PUT':
        print(request.data)
        kernel = Kernel_Service(1, request.data['dst'], request.data['cmd'])
        if request.data['dst'] == 'GestorArc':
            kernel.manage_directories(request.data['msg'])
        return Response(response, status=status.HTTP_200_OK)
