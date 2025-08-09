from django.shortcuts import render,redirect
from.models import User,Query,Productinfo

# Create your views here.

def home(req):
    return render(req,"home.html")
def register(req):
    print(req.POST)
    if req.method=="POST":
        name=req.POST.get('name')
        email=req.POST.get('email')
        password=req.POST.get('password')
        confirmpass=req.POST.get('confirmpass')
        profile=req.FILES.get('profile')
        print(profile)
        match=User.objects.filter(email=email)
        if match:
            msg="This email is already exist"
            return render(req,"register.html",{"msg":msg})
        else:
            if confirmpass==password:
                User.objects.create(name=name,email=email,password=password,confirmpass=confirmpass,profile=profile)
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
        if email == "viplovesana90@gmail.com" and password =="Viplove@123":
            msg ="Welcome Admin"
            return render(req,"admin_dashboard.html",{"welcome":msg})
        else:
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

def edit(req,id,pk):
    print(id,pk)
    editdata=Query.objects.get(id=id)
    userdata=User.objects.get(id=pk)
    return render(req,"user_dashboard.html",{"userpro":userdata,"editdata":editdata})

def update(req,id,pk):
    if req.method == "POST":
        name=req.POST.get("name")
        email=req.POST.get("email")
        query1=req.POST.get("query")
        olddata=Query.objects.get(id=id) 
        print(name,email,query1,olddata) 
        olddata.query=query1
        olddata.save() 
        aquery=Query.objects.filter(email=email)
        userdata=User.objects.get(id=pk)
        return render(req,"user_dashboard.html",{"userpro":userdata,"aquery":aquery})       
      
def delete(req,id,pk):
    deletedata=Query.objects.filter(id=id)
    if deletedata:
        deletedata=Query.objects.get(id=id)
        deletedata.delete()
        userdata=User.objects.get(id=pk) 
        aquery=Query.objects.filter(email=userdata.email) 
        return render(req,"user_dashboard.html",{"userpro":userdata,"aquery":aquery}) 
    else:
        userdata=User.objects.get(id=pk) 
        aquery=Query.objects.filter(email=userdata.email) 
        return render(req,"user_dashboard.html",{"userpro":userdata,"aquery":aquery}) 


from django.db.models import Q
def search(req,pk):
    userdata=User.objects.get(id=pk)
    searchdata=req.POST.get("search")
    aquery=Query.objects.filter(Q(email=userdata.email)&Q(query__contains=searchdata)) 
    return render(req,"user_dashboard.html",{"userpro":userdata,"aquery":aquery}) 



# .....................Admin dashboard code.......................................................


def proform(req):
    add="Wellcome Admin Please proceed"
    return render(req,"admin_dashboard.html",{'add':add})

def additem(req):
    if req.method == "POST":
        pro_name=req.POST.get('pro_name')
        pro_price=req.POST.get('pro_price')
        pro_mrp=req.POST.get('pro_mrp')
        pro_image=req.FILES.get('pro_image')
        pro_disc=req.POST.get('pro_disc')
        Productinfo.objects.create(pro_name=pro_name,pro_price=pro_price,pro_image=pro_image,pro_disc=pro_disc,pro_mrp=pro_mrp)
        return render(req,"admin_dashboard.html")
def dash(req):
     return render(req,"admin_dashboard.html")

def allproduct(req):
    itemdata=Productinfo.objects.all()
    return render(req,'allproducts.html',{'product':itemdata}) 
   
def carddetail(req,pk):
    itemdata=Productinfo.objects.get(id=pk)
    return render(req, 'card_detail.html', {'product': itemdata})

def addtocart(req,pk):
    if req.method == "POST":
        quantity = req.session.get( 'quantity',[])
        cart = req.session.get( 'cart',[])
        quan = int(req.POST.get( 'quantity' ))
        if pk not in cart:
            quantity.append(quan)
            cart.append(pk) 
        req.session['quantity'] = quantity
        req.session['cart'] = cart
        itemdata = Productinfo.objects.get(id=pk)
        return render(req,'card_detail.html',{'product':itemdata})
    return render(req,'card_detail.html')

def usercart(req):
    return render(req,'usercart.html')
