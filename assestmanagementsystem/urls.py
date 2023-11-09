"""
URL configuration for assestmanagementsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('login/addemp',views.addemp,name='addemp'),
    path('login/comcat',views.comcat,name='comcat'),
    path('login/comedit',views.comedit,name='comedit'),
    path('login/lapcat',views.lapcat,name='lapcat'),
    path('login/lapedit',views.lapedit,name='lapedit'),
    path('login/otheracc',views.otheracc,name='otheracc'),
    path('login/otheraccedit',views.otheraccedit,name='otheraccedit'),
    path('login/viewemployee',views.viewemployee,name='viewemployee'),
    path('login/addassests',views.addassests,name='addassests'),
    path('login/viewass',views.viewass,name='viewass'),
    path('login/viewass/addass/<int:id>',views.addass,name='addass'),
    path('login/viewass/addass/viewreass/<int:id>',views.viewreass,name='viewreass'),
    path('login/viewass/addass/viewreturn/<int:id>',views.viewreturn,name='viewreturn'),
    path('login/viewass/assass/viewreturn/viewfulldetails/<int:id>',views.viewfulldetails,name='viewfulldetails')
]
