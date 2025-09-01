"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('userdash/', views.userdash, name='userdash'),
    path('admindash/', views.admindash, name='admindash'),   
    path('logout/', views.logout, name='logout'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('query/<int:pk>/', views.query, name='query'),
    path('querydata/<int:pk>/', views.querydata, name='querydata'),
    path('allquery/<int:pk>/', views.allquery, name='allquery'),
    path('edit/<int:id>/<int:pk>', views.edit, name='edit'),
    path('update/<int:id>/<int:pk>', views.update, name='update'),
    path('delete/<int:id>/<int:pk>', views.delete, name='delete'),
    path('search/<int:pk>/', views.search, name='search'),
    path('productlist/', views.productlist, name='productlist'),
    path('searchproduct/', views.menusearch, name='menusearch'),
    path('productdelete/<int:id>/', views.productdelete, name='productdelete'),

    path('proform/', views.proform, name='proform'),
    path('additem/', views.additem, name='additem'),
    path('dash/', views.dash, name='dash'),
    path('allproduct/', views.allproduct, name='allproduct'),
    path('carddetail/<int:pk>/', views.carddetail, name='carddetail'),
    path('addtocart/<int:pk>/', views.addtocart, name='addtocart'),
    path('usercart/', views.usercart, name='usercart'),
    path('remove_cart/<int:pk>', views.remove_cart, name='remove_cart'),
    path('adress/', views.checkout, name='checkout'),   
    path('payment/',views.payment,name='payment'),
    path('paymenthandle/',views.paymenthandle,name='paymenthandle'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
