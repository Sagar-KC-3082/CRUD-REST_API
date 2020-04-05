from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(('POST',))
def CreateApiView(request):
    if request.method=="POST":
        x = CustomerSerializer(data=request.data)
        msg = {}
        if x.is_valid():
            x.save()
            msg["success"] = "create success!!!"
        else :
            msg["success"]="create unsuccessfull!!!"
        return Response(data=msg)



@api_view(('GET',))
def ReadApiView(request,pk):
    obj = customer.objects.get(id=pk)
    if request.method=="GET":
        x = CustomerSerializer(obj)
        return Response(x.data)




@api_view(('PUT',))
def UpdateApiView(request,pk):
    obj = customer.objects.get(id=pk)
    if request.method=="PUT":
        x = CustomerSerializer(obj,data=request.data)
        msg = {}
        if x.is_valid():
            x.save()
            msg['success']="update successful!!!"
        else :
             msg['success']="update not success!!!"
        return Response(data=msg)


@api_view(('DELETE',))
def DeleteApiView(request,pk):
    obj = customer.objects.get(id=pk)
    msg = {}
    if request.method=="DELETE":
        obj.delete()
        msg['success'] = "delete success!!!"
        return Response(data=msg)
