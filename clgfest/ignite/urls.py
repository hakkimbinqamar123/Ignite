from django.urls import path
from ignite import views
from django.contrib import admin
from . import views

urlpatterns=[
    path('',views.home, name="home"),
    path('events', views.events),
    path('registration', views.registration),
    path('product_details/<int:event_id>', views.product_details),
    path('login', views.login),
    path('stud_home', views.stud_home),
    path('base', views.base),
    path('results', views.results),
    path('schedule', views.schedule),
    path('payment', views.payment),
    path('confirm_payment', views.confirm_payment),
    path('judgehome', views.judgehome),
    path('logout',views.logout_view),
    path('results1/<int:event_id>',views.results1),
    path('contact',views.contact),
    path('stud_profile',views.stud_profile),
    path('edit_stud_profile',views.edit_stud_profile),
    path('stud_base',views.stud_base),
    path('stud_events',views.stud_events),
    path('stud_results',views.stud_results),
    path('stud_results1/<int:event_id>',views.stud_results1),
    path('stud_prod_details/<int:event_id>',views.stud_prod_details),
    path('product_details/events',views.events),
    path('stud_prod_details/events',views.events),
    path('results1/events',views.events),
    path('results1/login',views.login),
    path('results1/registration',views.registration),
    path('results1/results',views.results),
    path('result_upload',views.result_upload),
    path('judge_base',views.judge_base),
    path('judge_prod_details/<int:event_id>',views.judge_prod_details),
    path('judge_profile',views.judge_profile),
    path('edit_judge_profile',views.edit_judge_profile),
    path('judge_results',views.judge_results),
    path('judge_results1/<int:event_id>', views.judge_results1, name='judge_results1'),
    path('judge_results1/judgehome', views.judgehome, name='judge_results1'),
    path('judge_events',views.judge_events),
 

    
]