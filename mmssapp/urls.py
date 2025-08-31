
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home_page' ),
    path('views/', views.view, name='views_page'),
    path('create_manager/', views.Create_Manager, name='create_manager'),
    path('create_document/', views.create_document, name='document_page'),
    path('create_details', views.Create_Details, name='create_details'),
    path('create_boder/', views.Create_Boder, name='create_boder'),
    path('register_page/', views.Register_User, name='Register_Page'),
    path('login_page/', views.Login_Page, name='login_page')
]