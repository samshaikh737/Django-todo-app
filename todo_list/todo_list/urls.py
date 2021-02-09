
from django.contrib import admin
from django.urls import path
from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #my_url
    path('',views.home,name = 'home'),
    path('delete/<int:id>/',views.delete_item,name='delete'),
]
