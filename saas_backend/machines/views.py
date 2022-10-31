import json

from django.shortcuts import render
from django.http import JsonResponse
from . models import Machine_details,Machine_tech_details
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Machine_detailsSerializer,Machine_technicalSerializer,Machines_Serializer


# Create your views here.

@api_view(["GET"])
def machine_list(request):
    machine_list = []
    machine_data = Machine_details.objects.all()
    #print(machine_data)
    data ={}
    if machine_data:
        for obj in machine_data:
            # data["machine_id"] = obj.machine_id
            # data["machine_name"] = obj.machine_name
            # data["machine_model"] = obj.machine_model
            #data = model_to_dict(obj, fields=['machine_id','machine_name','machine_model'])

            data = Machines_Serializer(obj).data
            machine_list.append(data)

    return Response(machine_list)


@api_view(["GET","POST"])
def machine_info(request):
    req_data = request.data
    print('req_data ',req_data)
    serializer = Machines_Serializer(data=req_data)
    if serializer.is_valid():
        print("valid data")
    else:
        print(serializer.errors)
        print("data not valid")
    try:
        info_data = Machine_details.objects.filter(machine_id=req_data['machine_id'])
        tech_data = Machine_tech_details.objects.filter(machine_id=req_data['machine_id'])
        info_data_ser = Machine_detailsSerializer(info_data[0]).data
        if tech_data:
            tech_details = []
            for obj in tech_data:
                tech_data_ser = Machine_technicalSerializer(obj).data
                tech_details.append(tech_data_ser)
        return Response({"info":info_data_ser,"tech_details":tech_details})
    except:
        return Response({"select machine"})
