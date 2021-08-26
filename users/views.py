from pointages.settings import SECRET_KEY
from users.models import *
from users.serializers import *
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt , datetime




class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        login= request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=login).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        employes_serializer = UserSerializer(user) 

        response.data = {
            'jwt': token,
            'data':employes_serializer.data

        }

        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        # user = User.objects.filter(id=payload['username']).first()
        user = User.objects.get(username=payload['username']) 
        employes_serializer = UserSerializer(user) 
        return Response(employes_serializer.data) 


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response



@api_view(['GET','DELETE'])
def employes_list(request):
        # GET list of employes
        if request.method == 'GET':
            cordonnes = User.objects.all()
            cordonnes_serializer =UserSerializer(cordonnes, many=True)
            return Response(cordonnes_serializer.data)
        #  POST a new employe,
        # elif request.method == 'POST':
        #     data = JSONParser().parse(request)
        #     tutorial_serializer =UserSerializer(data=data)
        #     if tutorial_serializer.is_valid():
        #         tutorial_serializer.save()
        #         return Response( status=status.HTTP_201_CREATED) 
        #     else:
        #         return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # # DELETE all employes
        # elif request.method == 'DELETE':
        #     count = User.objects.all().delete()
        #     return Response({'message': '{} employes were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)




@api_view(['GET', 'PUT', 'DELETE'])
def employe_detail(request,username):
        # find employe by pk (id)
        try: 
                user = User.objects.get(username=username) 
        except User.DoesNotExist: 
                return Response({'message': 'The employe does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        if request.method == 'GET': 
            employes_serializer = UserSerializer(user) 
            return Response(employes_serializer.data) 
        
        # put a employe
        elif request.method == 'PUT': 
            data = JSONParser().parse(request) 
            employes_serializer = UserSerializer(user, data=data) 
            if employes_serializer.is_valid(): 
                employes_serializer.save() 
                return Response( status=status.HTTP_201_CREATED) 
            return Response(employes_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
            
        # delete an employe by pk
        elif request.method == 'DELETE': 
            user.delete() 
            return Response({'message': 'employe was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','POST','DELETE'])
def salaires(request):
        # GET list of salaires
        if request.method == 'GET':
            salaires = salaire.objects.all()
            salaires_serializer =salaireSerializer(salaires, many=True)
            return Response(salaires_serializer.data)
        #  POST a new salaire
        elif request.method == 'POST':
            data = JSONParser().parse(request)
            tutorial_serializer =salaireSerializer(data=data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return Response(status=status.HTTP_201_CREATED) 
            return Response(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # DELETE all salaires
        elif request.method == 'DELETE':
            count = salaire.objects.all().delete()
            return Response({'message': '{} salaires were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def employes_salaire(request,user):
    # find salaire by pk (id)
    try: 
            salaire_user = salaire.objects.get(user=user) 
    except salaire.DoesNotExist: 
              return Response({'message': 'The salary does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        salaire_serializer = salaireSerializer(salaire_user) 
        return Response(salaire_serializer.data) 
    
    # put a salaire
    elif request.method == 'PUT': 
        data = JSONParser().parse(request) 
        salaire_serializer = salaireSerializer(salaire_user, data=data) 
        if salaire_serializer.is_valid(): 
            salaire_serializer.save() 
            return Response( status=status.HTTP_201_CREATED) 
        return Response(salaire_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    # delete a employe by pk
    elif request.method == 'DELETE': 
        salaire_user.delete() 
        return Response({'message': 'salaire was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)




@api_view(['GET','POST','DELETE'])
def pointages(request):
        # GET list of pointage
        if request.method == 'GET':
            pointages = pointage.objects.all()
            pointage_serializer =pointageSerializer(pointages, many=True)
            return Response(pointage_serializer.data)
        #  POST a new pointage,
        elif request.method == 'POST':
            data = JSONParser().parse(request)
            pointage_serializer =pointageSerializer(data=data)
            if pointage_serializer.is_valid():
                pointage_serializer.save()
                return Response(status=status.HTTP_201_CREATED) 
            return Response(pointage_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # DELETE all pointage
        elif request.method == 'DELETE':
            count = pointage.objects.all().delete()
            return Response({'message': '{} pointage were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','PUT','DELETE'])
def employes_pointage(request, user):
    # find pointage by pk (id)
    try: 
            pointage_user = pointage.objects.get(user=user) 
    except pointage.DoesNotExist: 
              return Response({'message': 'The pointage does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        pointage_serializer = pointageSerializer(pointage_user) 
        return Response(pointage_serializer.data) 
    
    # put a pointage
    elif request.method == 'PUT': 
        data = JSONParser().parse(request) 
        pointage_serializer = pointageSerializer(pointage_user, data=data) 
        if pointage_serializer.is_valid(): 
            pointage_serializer.save() 
            return Response( status=status.HTTP_201_CREATED) 
        return Response(pointage_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    # delete a pointage by pk
    elif request.method == 'DELETE': 
        pointage_user.delete() 
        return Response({'message': 'pointage was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


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
def mission_detail(request,user):
    # find mission by pk (id)
    try: 
            mission_user = mission.objects.get(user=user) 
    except mission.DoesNotExist: 
              return Response({'message': 'The mission does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        missions_serializer = missionsSerializer(mission_user) 
        return Response(missions_serializer.data) 
    
    # put a mission
    elif request.method == 'PUT': 
        data = JSONParser().parse(request) 
        missions_serializer = missionsSerializer(mission_user, data=data) 
        if missions_serializer.is_valid(): 
            missions_serializer.save() 
            return Response( status=status.HTTP_201_CREATED) 
        return Response(missions_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    # delete a mission by pk
    elif request.method == 'DELETE': 
        mission_user.delete() 
        return Response({'message': 'mission was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def demarrer_mission(pk):    
    mission_pk = mission.objects.get(pk=pk) 
    data = mission_pk.objects.update(état="en exécution") 
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

