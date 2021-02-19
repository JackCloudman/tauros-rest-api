from django.contrib import admin
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','validated','owner')
    
admin.site.register(Profile,ProfileAdmin)