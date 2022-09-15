from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def fraud(request):
    return render(request,'fraud.html')

def learn(request):
    return render(request,'learn.html')

def locate(request):
    return render(request,'locate.html')

def vote(request):
    return render(request,'vote.html')

def report(request):
    return render(request,'report.html')

def lge(request):
    return render(request,'lge.html')
    
def ward(request):
    return render(request,'ward.html')

def verify(request):
    return render(request,'verify.html')

def hausa(request):
    return render(request,'hausa.html')

def next(request):
    return render(request,'next.html')