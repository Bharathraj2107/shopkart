from django.db import models
from django.contrib.auth.forms import UserCreationForm #get user name ,password from this model and we are going to override it
from django.contrib.auth.models import User
import datetime#when we upload the  image with same name say test.jpg it will be overwritten so each time when we upload we upload along with time and change the name the file will not overwrite
import os #to get the path 
# Create your models here.


def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")#dont add any comma at the end it will treat it as tuple if we add , 
    new_filename="%s%s"%(now_time,filename)#format string here time and filename will be concatenated and stored in filename
    #in current os path it should go and store in the folder called upload so i am going to return upload folder name
    return os.path.join('uploads/',new_filename)#what this function does is it take the given file and store the time in the now_time variable and join along with the given filename it gives new name +current path upload folder along with filename it will return
class Category(models.Model):#model will convert the class attribute to the database content
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)#to store the image here the getFilename function will be called and the uploads file will be created inside the static folder and the image will be stored there
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")#status do you want to show category or not it will be like checkbox
    created_at=models.DateTimeField(auto_now_add=True)#when this category is created the date and time will be saved
    def __str__(self):
        return self.name#here we are returning only name if we want to return our required fields then we need to overwrite see in the admins.py
class Product(models.Model):#model will convert the class attribute to the database content
    #we are going to link 2 tables so  we need common column so we declare the category column
    category=models.ForeignKey(Category,on_delete=models.CASCADE)#category is a foreign key in that model name == name of the category model if matches fetch all the items of that category
    name=models.CharField(max_length=150,null=False,blank=False)
    vendor=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)#to store the image here the getFilename function will be called and it will return and upload to the  upload_to location
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")#status do you want to show category or not it will be like checkbox
    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")#if the product is trending or not
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)#here user model is passed as parameter
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)#we need product which user selected for that
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.product_qty*self.Product.selling_price   
class Favourite(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)#to identify which user 
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)#to identify which product
    created_at=models.DateTimeField(auto_now_add=True)#time
