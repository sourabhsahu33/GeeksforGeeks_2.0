from django.urls import path
from .views import *

urlpatterns = [

    # ===================== Login page URL =============
    path('logout/', custom_logout, name="logout"),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),

    # ================ Home Page URL ==================
    path('', index, name='index'),
    path('about/', about , name ='about'),
    path('courses/', courses, name='courses'),
    path('contact/', contact, name='contact'),

    # ================ RoadMap URL ==============
    path('blog/', blog , name='blog'),

    # =============== Hackathon Page URL==============
    path('filter/', filter, name='filter'),
    path('alarm/', alarm, name='alarm'),
    
    # =============Resume URL ==================
    path('resume_form/', resume_form, name='resume_form'),
    path('resume/', resume, name='resume'),
    
    # ===============Compiler URL =================
    path('compiler/', compiler, name="compiler"),
    path('runcode', runcode, name="runcode"),
    
    # =======Calcualator================
    path('cgpa_calculator/', cgpa_calculator, name='cgpa_calculator'),
    path('edit/<int:subject_id>/', edit_subject, name='edit_subject'),
    path('delete/<int:subject_id>/', delete_subject, name='delete_subject'),
    path('result/', result, name='result'),
    
]
