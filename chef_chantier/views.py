from chef_chantier.models import *
from django.shortcuts import render
from rest_framework.decorators import api_view
from chef_chantier.serializers import *
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET','POST','DELETE'])
def missions(request):
        # GET list of missions
        if request.method == 'GET':
            missions = mission.objects.all()
            missions_serializer =missionsSerializer(missions, many=True)
            return Response(missions_serializer.data)

        #  POST a new mission,
        if request.method == 'POST':
            data = JSONParser().parse(request)
            missions_serializer = missionsSerializer(data=data)
            if missions_serializer.is_valid():
                missions_serializer.save()
                return Response( status=status.HTTP_201_CREATED) 
            return Response(missions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # DELETE all missions
        elif request.method == 'DELETE':
            count = mission.objects.all().delete()
            return Response({'message': '{} missions were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def mission_detail(request, pk):
    # find mission by pk (id)
    try: 
            mission_pk = mission.objects.get(pk=pk) 
    except mission.DoesNotExist: 
              return Response({'message': 'The mission does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        missions_serializer = missionsSerializer(mission_pk) 
        return Response(missions_serializer.data) 
    
    # put a mission
    elif request.method == 'PUT': 
        data = JSONParser().parse(request) 
        missions_serializer = missionsSerializer(mission_pk, data=data) 
        if missions_serializer.is_valid(): 
            missions_serializer.save() 
            return Response( status=status.HTTP_201_CREATED) 
        return Response(missions_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    # delete a mission by pk
    elif request.method == 'DELETE': 
        mission_pk.delete() 
        return Response({'message': 'mission was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def demarrer_mission(request, pk):    
    mission_pk = mission.objects.get(pk=pk) 
    data = mission.objects.update(état="en exécution") 
    missions_serializer = missionsSerializer(mission_pk, data=data) 
    if missions_serializer.is_valid(): 
        missions_serializer.save() 
        return Response(missions_serializer.data) 
    return Response(missions_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['PUT'])
def terminer_mission(request, pk):    
    mission_pk = mission.objects.get(pk=pk) 
    data = mission.objects.update(état="terminé") 
    missions_serializer = missionsSerializer(mission_pk, data=data) 
    if missions_serializer.is_valid(): 
        missions_serializer.save() 
        return Response(missions_serializer.data) 
    return Response(missions_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
