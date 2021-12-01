from django.contrib import admin
from django.urls import path
from myapp.views import MyLogin, MyRegister, MyLogOut, HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('login/', MyLogin.as_view(), name='login'),
    path('register/', MyRegister.as_view(), name='register'),
    path('logout/', MyLogOut.as_view(), name='logout'),
]
