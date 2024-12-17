from django.contrib import admin
from .models import* #if we want all the models 
# class CategoryAdmin(admin.ModelAdmin):
#     list_display=('Name','Image','Description')#all this fields will be displayed in the admin category table when we login as admin and the field names and the model names should be same
#admin.site.register(Category,CategoryAdmin)
admin.site.register(Category)
admin.site.register(Product)
# Register your models here.
#if we want to change the theme of the admin then pip install django-jazzmin
#username=bharath same for pwd

