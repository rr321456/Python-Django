from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def print_hello(request):
    movie_data={ 'movies' : [{
        'title':'GodFather',
        'year':1990,
        'sucess':False
    },
    {
        'title':'Into the world',
        'year':2009,
        'summary':'story of an underworld',
        'sucess':True
    },{
        'title':'Titanic',
        'year':2002,
        'summary':'story of an underworld',
        'sucess':False
    },{
        'title':'Goldfish',
        'year':1980,
        'summary':'story of an underworld',
        'sucess':False
    },]}
    return render(request,'hello.html',movie_data)