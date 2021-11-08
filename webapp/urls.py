from django.urls import path
from webapp import views 
from django.conf.urls.static import static
from django.conf import  settings

urlpatterns = [
    path('',views.home_view,name="home"),
    path('about-detailes/',views.about_view,name="about"),
    path('webportal-detailes/',views.webportal_view,name="webportal"),

 

    path('task-detailes',views.Task_view,name="task"),
    # path('',views.home_view,name="home"),

    path('assignment-detailes/',views.assignment_view,name="create-data"),

    path('employe/',views.employe,name="employe"),


    path('show-assignment/',views.allassignment_view,name='showdata'),


    # user creation form
    path('reg/',views.registration_view,name="registration"),
    # login page
    path('login/',views.login_view,name="login"),




]

if settings.DEBUG:
    urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
