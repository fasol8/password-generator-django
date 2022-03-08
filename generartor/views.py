from random import random
from django.shortcuts import render
import random
# from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):

    characters=list('abcdefghijklmnñopqrstuvwxyz')
    generator_password=''
    length=int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%&/()?¿¡^*+Ç¨_.-:,;'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    for x in range(length):
        generator_password+=random.choice(characters)

    return render(request,'password.html',{'password':generator_password})
