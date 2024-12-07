from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from app.serializers import *
from app.models import *
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def Empdata(request):
    jso = Emp.objects.all()  # Call the method to get the queryset
    leo = Empmodel(jso, many=True)  # Pass the queryset to the serializer
    return Response(leo.data)