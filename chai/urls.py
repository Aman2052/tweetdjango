#from django.contrib import admin not needed
from django.urls import path
#current directory me se view import karo
from . import views
#local host :8000/chai
# localhost:8000/chai/order
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.all_chai, name='all_chai'),
    #path('order/', views.order, name='order'),
    # path('about/',views.about, name='about'),
    # path('contact/',views.contact, name='home'),
]