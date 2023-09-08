"""
URL configuration for college project.

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
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index,name="home"),
    path('adm/',views.admin,name="adminstration"),
    path('adlog/',views.adlog,name="adlog"),
    path('super/',views.super,name="super"),
    path('a_logout/',views.a_logout,name="a_logout"),
    path('add_student',views.ad_student,name="add_student"),
    path('add_teacher',views.ad_teacher,name="add_teacher"),
    path('add_principal',views.p_update,name="add_principal"),


    path('p_delete/<str:pk>',views.p_delete,name="p_delete"),

    path('Student_view/',views.s_view,name="s_view"),
    path('s_delete/<str:pk>',views.s_delete,name="s_delete"),

    path('teacher_view/',views.t_view,name="t_view"),
    path('principal_view/',views.p_view,name="p_view"),

    path('studentlogin/',views.s_login,name="s_login"),
    path('s_validate/',views.s_check,name="s_validate"),
    path('s_logout/',views.s_logout,name="s_logout"),
    path('s_log/',views.s_log,name="s_log"),
    path('s_marklist/',views.s_marklist,name="s_marklist"),
    path('s_profile/',views.s_profile,name="s_profile"),
    path('s_profile_update/',views.s_pro_update,name="s_profile_update"),
    path('s_profile_update2/',views.s_pro_update2,name="s_profile_update2"),
    path('s_leave',views.s_leave,name="s_leave"),
    path('s_add_leave',views.s_add_leave,name="s_add_leave"),
    path('s_notefiles',views.s_notes,name="s_notefiles"),
    path('s_notify',views.s_notify,name="s_notify"),
  
    
    
     
   
    

    path('t_loghome/',views.t_loghome,name="t_loghome"),
    path('teacherlogin/',views.t_login,name="t_login"),
    path('t_validate/',views.t_check,name="t_validate"),
    path('t_logout/',views.t_logout,name="t_logout"),
    path('t_log/',views.t_log,name="t_log"),
    path('t_upmark/',views.t_upmark,name="t_upmark"),
    path('t_uploadmark/',views.t_uploadmark,name="t_uploadmark"),
    path('t_updatemark',views.t_updatemark,name="t_updatemark"),
    
    path('t_m_list/',views.t_m_list,name="t_m_list"),
    path('t_m_updatelist/<str:pk>',views.t_m_update,name="t_m_updatelist"),
    path('t_leave',views.t_leave,name="t_leave"),
    path('t_veiwleave/<str:pk>',views.t_viewleave,name="t_viewleave"),
    path('t_work_view',views.t_work_view,name="t_work_view"),
    path('t_work_home',views.t_work_home,name="t_work_home"),
    path('t_w_status/<str:pk>',views.t_w_status,name="t_w_status"),
    path('t_notice',views.t_notice,name="t_notice"),
    path('t_profile_update/',views.t_profile_update,name="t_profile_update"),
    path('t_profile_update2/',views.t_profile_update2,name="t_profile_update2"),

    path('p_login',views.p_login,name="p_login"),
    path('p_validate/',views.p_check,name="p_validate"),
    path('p_log/',views.p_log,name="p_log"),
    path('p_logout/',views.p_logout,name="p_logout"),
    path('p_profile/',views.p_profile,name="p_profile"),
    path('p_profile2/',views.p_profile2,name="p_profile2"),
    path('p_students/',views.p_students,name="p_students"),
    path('p_search/',views.p_search,name="p_search"),

    
    



    


]
