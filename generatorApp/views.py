from django.shortcuts import render
from string import ascii_lowercase, ascii_uppercase, digits
import random
def home(request):
    dct = {'title': 'MainPage', 'length': [x for x in range(5, 13)]}
    return render(request, 'generatorApp/index.html', context=dct)

def password(request):
    characters = ascii_lowercase
    if request.GET.get('numbers', None):
        characters += digits
    if request.GET.get('uppercase', None):
        characters += ascii_uppercase
    if request.GET.get('characters', None):
        characters += '!@#$%^&*?/'
    password = ''.join([random.choice(list(characters)) for x in range(int(request.GET.get('length')))])
    dct = {'title': 'Generated Pass', 'password': password}
    return render(request, 'generatorApp/password.html', context=dct)
