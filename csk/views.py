from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def msd(request):
    return render (request,'msd.html')

def pathirana(request):
    return HttpResponse('<h1><marquee>BEST BOWLER IN CSK TEAM</marquee></h1>')