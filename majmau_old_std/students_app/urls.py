from django.urls import path, include
from . import views

urlpatterns = [
    path('home/',views.index, name='home'),
    path('',views.registration, name='registration'),
    path('login/',views.sign_in, name='login'),
    path('logout/',views.log_out, name='logout'),
    path('export/', views.export_students_to_excel, name='export')


]