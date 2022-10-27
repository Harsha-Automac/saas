from django.shortcuts import render
from django.http import JsonResponse
from . models import Machine_details

# Create your views here.
def machine_list(request):
    machine_list = []
    machine_data = Machine_details.objects.all()
    print(machine_data)
    print(machine_data[0].machine_id)
    data ={}
    if machine_data:
        for obj in machine_data:
            data["machine_id"] = obj.machine_id
            data["machine_name"] = obj.machine_name
            data["machine_model"] = obj.machine_model
            machine_list.append(data)

    return JsonResponse({"machine_data":machine_list})