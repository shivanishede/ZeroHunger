from django.urls import path
from . import views


from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_view, name='about'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('information/', views.information_view, name='information'),
    path('logout/', views.logout_view, name='logout'),
    path('donar/', views.donar_view, name='donar'),
    path('receiver/', views.receiver_view, name='receiver'),
    path('donarinfo/', views.donarinfo, name='donarinfo'),
    path('submit_donar_info/',views.submit_donar_info, name='submit_donar_info'),
    path('receiverview/', views.receiverview, name='receiverview'),
    path('donarview/', views.donarview, name='donarview'),
    path('editdonar/<int:donar_id>/', views.editdonar, name='editdonar'),
    path('save_donar_info/', views.save_donar_info, name='save_donar_info'),
    path('deletedonar/', views.deletedonar, name='deletedonar'),
    path('certificate/', views.certificate, name='certificate'),
    path('success/', views.success, name='success'),
    
]



