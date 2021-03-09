from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

    



urlpatterns = [
    path('admin/', views.admin,name='admin'),
    path("",views.index,name=''),
    path("login",views.loginpage,name='login'),
    path("register",views.register,name='register'),
    path("logout",views.logoutUser,name='logout'),
    path("cours",views.cours,name='cours'),
    path("contact",views.contact,name='contact'),
    path("forms",views.formpage,name='forms'),
    path("student",views.student,name='student'),
    path("error",views.error,name='error'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


