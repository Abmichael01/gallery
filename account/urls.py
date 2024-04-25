from django.urls import path
from . views import *

urlpatterns = [
    path('login/', loginUser, name="login"),
    path('register/', registerUser, name="register"),
    path('logout/', logoutUser, name="logout"),
    path('deactivate/', deactivateUser, name="deactivate"),
]
