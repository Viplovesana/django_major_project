from django.shortcuts import render,redirect
from.models import User,Query,Productinfo

# Create your views here.

def home(req):
    userid = req.session.get('user_id')
    card=req.session.get('cart',[])
    if userid:
        if card:
             count=len(card)
             return render(req,"home.html",{'count':count ,'userid':userid})
        return render(req,"home.html",{'userid':userid})
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
                    user_id= usermatch.id
                    req.session['user_id']=user_id         
                    return redirect('userdash')
                else:
                    msg="password not matched"
                    return render(req,"login.html",{"msg":msg})
            else:
                msg="Email not registerd"
                return render(req,"register.html",{"email":msg})        
    return render(req,"login.html")

def userdash(req):
    userid = req.session.get('user_id')
    if userid:
        userdata=User.objects.get(id=userid)
        return render(req,"user_dashboard.html",{"userpro":userdata,'userid':userid})   
    else:
       return redirect('login')

def logout(req):
    userid = req.session.get('user_id')
    if userid:
       del req.session['user_id']
       return redirect('home')
    return redirect('login')



                
def query(req,pk):
    userid = req.session.get('user_id')    
    userdata=User.objects.get(id=pk)
    return render(req,"user_dashboard.html",{"userpro":userdata,"query":pk,'userid':userid})

def querydata(req,pk):
    userid = req.session.get('user_id')
    if req.method == "POST":
        name=req.POST.get("name")
        email=req.POST.get("email")
        query=req.POST.get("query")
        Query.objects.create(name=name,email=email,query=query)
        userdata=User.objects.get(id=pk)
        aquery=Query.objects.filter(email=email)
        return render(req,"user_dashboard.html",{"userpro":userdata,"query":pk,"aquery":aquery,'userid':userid})      

def allquery(req,pk):
    userid = req.session.get('user_id')
    userdata=User.objects.get(id=pk)
    email=userdata.email
    aquery=Query.objects.filter(email=email)
    return render(req,"user_dashboard.html",{"userpro":userdata,"aquery":aquery,'userid':userid})

def edit(req,id,pk):
    userid = req.session.get('user_id')
    print(id,pk)
    editdata=Query.objects.get(id=id)
    userdata=User.objects.get(id=pk)
    return render(req,"user_dashboard.html",{"userpro":userdata,"editdata":editdata,'userid':userid})

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
    card=req.session.get('cart',[])
    if card:
        count=len(card)
        return render(req,'allproducts.html',{'product':itemdata,'count':count}) 
    return render(req,'allproducts.html',{'product':itemdata}) 
   
def carddetail(req,pk):
    itemdata=Productinfo.objects.get(id=pk)
    card=req.session.get('cart',[])
    if card:
        count=len(card)
        return render(req, 'card_detail.html', {'product': itemdata,'count':count})
    return render(req, 'card_detail.html', {'product': itemdata,})

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
        count=len(cart)
        return render(req,'card_detail.html',{'product':itemdata ,'count':count})
    return render(req,'card_detail.html')

def usercart(req):
    cart = req.session.get('cart',[])
    quantity = req.session.get('quantity',[])
    print(cart,quantity)
    l=[]
    totalprize=0
    totalsavings=0
    count=len(cart)
    for i ,j in zip(cart,quantity):
        pro_i = Productinfo.objects.get(id=i)
        data={
            'id':pro_i.id,
            'name':pro_i.pro_name,
            'disc':pro_i.pro_disc,
            'price':pro_i.pro_price,
            'mrp':pro_i.pro_mrp,
            'image':pro_i.pro_image,
            'quantity':j,
            'totalprice':pro_i.pro_price*j,
            'savings': pro_i.pro_mrp - pro_i.pro_price,
            'totalsavings':(pro_i.pro_mrp - pro_i.pro_price) * j
        }
        totalprize+=pro_i.pro_price*j
        totalsavings += (pro_i.pro_mrp - pro_i.pro_price) * j
        l.append(data)
       
    return render(req,'usercart.html',{'listdata':l,'totalprice':totalprize,'totalsavings':totalsavings,'count':count})

def remove_cart(req,pk):
    cart = req.session.get( 'cart',[])
    quantity = req.session.get( 'quantity',[])
    rindex = cart.index(pk)
    if pk in cart:
        del cart[rindex]
        del quantity[rindex]
        req.session['cart']=cart
        req.session['quantity']=quantity
        req.session.modified=True
        return redirect('usercart')
    else:
        return redirect('usercart')
