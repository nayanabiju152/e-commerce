from django.shortcuts import render,redirect
from .models import user,prd

# Create your views here.
def log(request):
    return render(request,'login.html')



def reg(request):
    return render(request,'registration.html')



def hom(request):
    data=prd.objects.all()
    for i in data:
        print(i.prd_name)
    return render(request,'home.html',{'data':data})

def log_btn(request):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        print(name)
        print(password)
        if user.objects.filter(name=name, password=password).exists():
            print("<<<<<>>>>>>>>>")
            return redirect('home')
        else:return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        name = request.POST.get('Username')
        passs = request.POST.get('password')
        Em = request.POST.get('Email')
        ph = request.POST.get('phone no')
        add = request.POST.get('address')
        
        print(name)
        print(passs)
        print(Em)
        print(ph)
        print(add)
        user.objects.create(name=name, password=passs,Email=Em,ph=ph,add=add)
        return redirect('login')
    return render(request,'registration.html')