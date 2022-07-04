from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . db import *
from . models import *
import os
from datetime import datetime

# Create your views here.

@api_view(['GET'])
def index(request):
    message = 'Congratulations, you  have created an API'
    return Response(message)

@api_view(['POST'])
def user_login(request):
    username = request.data['username']
    print(request.data)
    password = request.data['password']
    print(username)
    print(password)
    login = Login(username, password)
    result = login_db(login)
    return Response(result)


@api_view(['POST'])
def user_register(request):
    first_name = request.data['first_name']
    last_name = request.data['last_name']
    gender = request.data['gender']
    dob = request.data['dob']
    email = request.data['email']
    username = request.data['email'] 
    phone = request.data['phone']
    password = request.data['password']

    #add to registered users
    user = User(first_name, last_name, gender, dob, email, phone)
    print(user)
    user_id = register_db(user)
    #add to login table
    login = Login(username,password)
    status = insertLogin_db(user_id, login)

    return Response(status)

@api_view(['POST'])
def updatePassword(request):
    username = request.data['username']
    current_password = request.data['current_password']
    new_password = request.data['new_password']
    update = update_password_db(username, current_password, new_password)
    return Response(update)

@api_view(['POST'])
def insert_post(request):
    username = request.data['username']
    content = request.data['content']
    created_time = datetime.now()
    post = Post(username, content, created_time)
    insert = insertPost_db(post)
    return Response(insert)

@api_view(['POST'])
def delete_post(request):
    post_id = request.data['post_id']
    delete = deletePost_db(post_id)
    return Response(delete)