from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

from .serializers import ProfileSerializer,CustomResponseSerializer
from .models import Profile,CustomResponse

@api_view(['POST'])
def create_account(request):
    response = CustomResponse()

    # DATOS FORMULARIO
    data = request.data
    email = data.get("email")
    password = data.get("password")

    # VALIDACION CORREO Y CONTRASEÑA
    if email == '' or email == None or password == '' or password == None:
        response.message = "Usuario o contraseña invalidos"
        return Response(status=status.HTTP_400_BAD_REQUEST,data=CustomResponseSerializer(response).data)
    # INTENTAMOS CREAR EL USUARIO
    try:
        user,created = User.objects.get_or_create(username=email,password=password,email=email)
    except:
        response.message = "El usuario ya existe"
        return Response(status=status.HTTP_400_BAD_REQUEST,data=CustomResponseSerializer(response).data)
    # SI SE CREO EL USUARIO DEVOLVEMOS MENSAJE DE EXITO Y EL TOKEN ASOCIADO
    if created:
        token = Token.objects.create(user=user)
        Profile.objects.create(owner=user)
        response.message = "Usuario creado con éxito"
        response.token = token
        return Response(status=status.HTTP_201_CREATED,data=CustomResponseSerializer(response).data)
    
    # SE CREO DE NUEVO EL USUARIO
    response.message = "El usuario ya existe"
    return Response(status=status.HTTP_400_BAD_REQUEST,data=CustomResponseSerializer(response).data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_profile(request):

    response = CustomResponse()
    profile = get_profile_by_token(request.auth.key)

    # Si el usuario ya fue validado devolvemos un mensaje
    if profile.validated:
        response.message = "Tu usuario ya ha sido validado"
        return Response(status=status.HTTP_400_BAD_REQUEST,data=CustomResponseSerializer(response).data)
    
    serializer = ProfileSerializer(data=request.data)

    # Validamos la información
    if serializer.is_valid():
        # Revisamos que los campos a editar esten en blanco y por lo tanto podrán ser modificados
        for key in serializer.fields:
            field_object = profile._meta.get_field(key)
            field_value = getattr(profile, field_object.attname)
            # Si es None o vacio el atributo original entonces lo modificaremos
            if field_value == None or field_value == "":
                setattr(profile,field_object.attname,serializer.data[key])
        # Guardamos
        profile.save()

        response.message = "Datos actualizados, en espera de aprobación"
        return Response(status=status.HTTP_200_OK,data=CustomResponseSerializer(response).data)
    else:
        response.message = "Los datos ingresados son erroneos"
        return Response(status=status.HTTP_400_BAD_REQUEST,data=CustomResponseSerializer(response).data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_me(request):
    profile = get_profile_by_token(request.auth.key)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)

# Obtenemos un usuario/Token por su token
def get_profile_by_token(token):
    user_id = Token.objects.get(key=token).user_id
    user = User.objects.get(id=user_id)
    return Profile.objects.filter(owner=user).first()