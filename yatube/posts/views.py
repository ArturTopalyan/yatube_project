#from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница со списком групп сообщества
def group_posts(request, slug):
    return HttpResponse(f'Cтраницы, на которых будут посты, отфильтрованные по группам {slug}')

# Create your views here.
