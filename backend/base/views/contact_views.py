from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from base.products import products
from base.models import Product, User
from base.serializers import ProductSerializer, UserSerializer, UserSerializerWithToken
from django.core.mail import send_mail

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.hashers import make_password
from rest_framework import status


@api_view(['POST'])
def contact(request):
    if request.method == 'POST':
        data = request.data 
        customer_email = data["email"]
        email = str(data)
        send_mail('Customer Query', 'This is the message', customer_email, ['dmackeyward@gmail.com'], html_message=email)
        return Response({'message': 'Data received and processed successfully.'})