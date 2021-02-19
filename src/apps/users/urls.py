from django.urls import path
from . import views

urlpatterns = [
    path('register',views.create_account,name="register"),
    path('me',views.get_me,name="GET me"),
    path('me/profile',views.update_profile,name="Update me ")
]