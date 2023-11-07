from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Movieform
from.models import Movie


# Create your views here.
def index(request):
    var=Movie.objects.all()
    dic={'mkey':var}
    return render(request,'index.html',dic)

def details(request,id):
    var2=Movie.objects.get(id=id)
    dic2={'m2key':var2}
    return render(request,'details.html',dic2)
def insert(request):
    if request.method=="POST":
        n=request.POST.get('n1')
        d=request.POST.get('n2')
        y = request.POST.get('n3')
        i = request.FILES['n4']
        x=Movie(movie_name=n, movie_desc=d,movie_year=y,movie_img=i)
        x.save()
    return render(request,'insert.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=Movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')