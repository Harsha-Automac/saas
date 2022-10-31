from rest_framework import serializers

from .models import Machine_details,Machine_tech_details

class Machines_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Machine_details
        fields=["machine_id","machine_name","machine_model",]


class Machine_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine_details
        fields='__all__'


class Machine_technicalSerializer(serializers.ModelSerializer):
    class Meta:
        #model = Machine_details
        model = Machine_tech_details
        fields=['machine_id','component_name']

