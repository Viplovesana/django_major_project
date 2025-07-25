from django.shortcuts import render
from.models import User,Query

# Create your views here.

def home(req):
    return render(req,"home.html")
def register(req):
    if req.method=="POST":
        name=req.POST.get('name')
        email=req.POST.get('email')
        password=req.POST.get('password')
        confirmpass=req.POST.get('confirmpass')
        match=User.objects.filter(email=email)
        if match:
            msg="This email is already exist"
            return render(req,"register.html",{"msg":msg})
        else:
            if confirmpass==password:
                User.objects.create(name=name,email=email,password=password,confirmpass=confirmpass)
                msg="data Stored successfully"
                return render(req,"login.html",{"msg":msg})
            else:
                pswd="Password not matched"
                return render(req,"register.html",{"pswd":pswd}) 
           
    return render(req,"register.html")
def login(req):
    if req.method == "POST":
        email=req.POST.get('email')
        password=req.POST.get('password')
        
        match=User.objects.filter(email=email)
        if match:
            usermatch=User.objects.get(email=email)
            pass1=usermatch.password
            if password==pass1:
                return render(req,"user_dashboard.html",{"userpro":usermatch})
            else:
                msg="password not matched"
                return render(req,"login.html",{"msg":msg})
        else:
            msg="Email not registerd"
            return render(req,"register.html",{"email":msg})        
    return render(req,"login.html")
def logout(req):
    pass
                
def query(req,pk):
    userdata=User.objects.get(id=pk)
    return render(req,"user_dashboard.html",{"userpro":userdata,"query":pk})
def querydata(req,pk):
    if req.method == "POST":
        name=req.POST.get("name")
        email=req.POST.get("email")
        query=req.POST.get("query")
        Query.objects.create(name=name,email=email,query=query)
        userdata=User.objects.get(id=pk)
        aquery=Query.objects.filter(email=email)
        return render(req,"user_dashboard.html",{"userpro":userdata,"query":pk,"aquery":aquery})      

def allquery(req,pk):
    userdata=User.objects.get(id=pk)
    email=userdata.email
    aquery=Query.objects.filter(email=email)
    return render(req,"user_dashboard.html",{"userpro":userdata,"aquery":aquery})          


          

