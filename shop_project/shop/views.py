from django.shortcuts import render,redirect
from .models import*#here from our app import all the models
from django.contrib import messages
from django.http import HttpResponse as HTTPResponse,JsonResponse
from shop.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout
import json
def home(request):
    products=Product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"products":products})

def favviewpage(request):
        if request.user.is_authenticated:#if login then only allow
         fav=Favourite.objects.filter(user=request.user)#here i  am taking all the favourite products
         return render(request,"shop/fav.html",{"fav":fav})
        else:
            return redirect("/")#redirect to home page

def remove_fav(request,fid):
    item=Favourite.objects.get(id=fid)
    item.delete()
    return redirect("/favviewpage")         
def cart_page(request):
    if request.user.is_authenticated:#if login then only allow
        cart=Cart.objects.filter(user=request.user)#here i want all the details of the user
        return render(request,"shop/cart.html",{"cart":cart})
    else:
        return redirect("/")#redirect to home page
    
def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/cart")    

def fav_page(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':#here we are checking  whether we getting the request through  the httprequest
      if request.user.is_authenticated:  #here we checking whether the user is logged in 
        data=json.load(request)#the data coming from the request is in the json format and i am assigning it to the data variable
        product_id=(data['pid'])
        product_status=Product.objects.get(id=product_id)#here we are checking product is there or not
        if product_status:
            if Favourite.objects.filter(user=request.user.id,Product_id=product_id):#we are checking if the product already exists in the cart
                 return JsonResponse({'status':'Product Already Exists in the Favourite'},status=200)
            else:
              Favourite.objects.create(user=request.user,Product_id=product_id)
              return JsonResponse({'status':'Product Added to  Favourite'},status=200)     
      else:
          return JsonResponse({'status':'Login to Add the Favourite'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)
def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':#here we are checking  whether we getting the request through  the httprequest
      if request.user.is_authenticated:  #here we checking whether the user is logged in 
        data=json.load(request)#the data coming from the request is in the json format and i am assigning it to the data variable
        product_qty=data['product_qty']
        product_id=(data['pid'])
        #print(request.user.id)
        product_status=Product.objects.get(id=product_id)#here we are checking product is there or not
        #if product is present then add to database or else it should show error message if alredy exists in the cart it should show the product already in the cart say already exist if not  then store it in the database
        if product_status:
            if Cart.objects.filter(user=request.user.id,Product_id=product_id):#1 product 2 or more users will be keeping it so we are checking here user and product id we are checking if matches product already exists
                return JsonResponse({'status':'Product Already Exists in the cart'},status=200)#here we are returning the response in json format to the ajax request that already exists
            else:
                if product_status.quantity>=product_qty:#if product not there then take the product quantity then check the stock then insert into the database
                    Cart.objects.create(user=request.user,Product_id=product_id,product_qty=product_qty)
                    return JsonResponse({'status':'Product Added to Cart '},status=200)
                else:
                    return JsonResponse({'status':'Product Stock Not Available '},status=200)
     
      else:
          return JsonResponse({'status':'Login to Add the products to the Cart'},status=200)
    else:
        return JsonResponse({'status':'Invalid Access'},status=200)

def logout_page(request):
    if request.user.is_authenticated:#here we are checking whether the user is logged in or not
        logout(request)#it is used for logging out the user
        messages.success(request,"Logged out Successfully")
        return redirect("/")
    
def login_page(request):
    if request.user.is_authenticated:#if user is logged in then in url if type /login it should not direct to the login page so we are directing it to the home page
        return redirect("/")
    else:
        if request.method=='POST':#here we are checking whether user requesting method is post
            name=request.POST.get('username')#inside the () name is the name of the input field
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)#this will authenticate the user to check if user data is correct or not
            if user is not None:#if user data is correct
                login(request,user)#this will create the session and login the user
                messages.success(request,"Logged in Successfully")
                return redirect('/')
            else:
                messages.error(request,"Invalid user Name or Password")   
                return redirect('/login') 
        return render(request,"shop/login.html")
    

def register(request):
    form=CustomUserForm()#we are calling this class and passing it as parameter to the template
    if request.method=='POST':#after the form submission we will get the post method
        form=CustomUserForm(request.POST)#users data will be stored in this form variable
        if form.is_valid():
            form.save()#by default it loads the error message
            messages.success(request,"Registration Success You can Login Now..!")
            return redirect('/login') 
    return render(request,"shop/register.html",{'form':form})

def collections(request):
    category=Category.objects.filter(status=0)#in our model status=0 means show and status=1 means hidden we are taking only the visible things here
    return render(request,"shop/collections.html",{"category":category})


def collectionsView(request,name):
   if(Category.objects.filter(name=name,status=0)).exists():#here we are checking if the entered category is in the category model
        products=Product.objects.filter(category__name=name,status=0)#here in products model the category is a foreign key in that model name == name of the category model if matches fetch all the items of that category  
        return render(request,"shop/products/index.html",{"products":products,"category_name":name})
   else:
       messages.warning(request,"No Such Category Found")
       return redirect('collections')
   

def product_details(request,cname,pname):
       if(Category.objects.filter(name=cname,status=0)).exists():#here we are checking if the entered category is in the category model
           if(Product.objects.filter(name=pname,status=0)).exists():#here we are checking if the entered product is in the product model
               products=Product.objects.filter(name=pname,status=0).first()#here we are fetching the product details of the clicked product in the particular category
               return render(request,"shop/products/product_details.html",{"products":products})
           else:
            messages.warning(request,"No Such Category Found")
            return redirect('collections') 
       else:
           messages.warning(request,"No Such Category Found")
           return redirect('collections')    