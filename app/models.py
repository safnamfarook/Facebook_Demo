from django.db import models

# Create your models here.

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #getters and setters, username and password -make it as private variables.

class User:
    def __init__(self, first_name, last_name, gender, dob, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.dob = dob
        self.email = email
        self.phone = phone

class Post:
    def __init__(self, username, content, created_time):
        self.username = username
        self.content = content
        self.created_time = created_time

