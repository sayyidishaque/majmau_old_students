from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('registration/',views.registration, name='registration'),
    path('login/',views.sign_in, name='login'),
    path('logout/',views.log_out, name='logout'),
    path('export/', views.export_students_to_excel, name='export')


]