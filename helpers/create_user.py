from faker import Faker
import requests
import pytest
from helpers import urls


fake = Faker(locale="ru_RU")

def create_name():
    name = fake.name()
    return name

def create_email():
    email = fake.email()
    return email

def create_password():
    password = fake.password()
    return password

def create_user():
    user_data = {'name': create_name(), 'email': create_email(), 'password': create_password()}
    return user_data

def register_user():
    user = create_user()
    register = urls.CREATE_USER
    payload = {
        'name': user['name'],
        'email': user['email'],
        'password': user['password']

    }
    headers = {'Content-Type': 'application/json'}
    response_register = requests.post(register, json=payload, headers=headers)

    return user, response_register

def delete_user(access_token):
    delete = urls.DELETE_USER
    headers =  {
        'Accept': 'application/json',
        'Authorization': f'{access_token}'
    }
    response_delete = requests.delete(delete, headers=headers)


