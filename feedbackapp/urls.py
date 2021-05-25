from django.urls import path

from feedbackapp.views import home,facultyhome,registerform,writefaculty,flogin,mainform,fs
from studentfeedbackapp.views import stdhome,stdreg,writestudent,slogin,s_cource_feedb,up_st_fee_co,s_faculty_feedb
from feedbackapp import views

urlpatterns=[

    path('',home,name='home'),
    path('facultyhome',facultyhome,name='facultyhome'),
    path('registerform',registerform,name='registerform'),
    path('writefaculty',writefaculty,name='writefaculty'),
    path('flogin',flogin,name='flogin'),
    path('mainform',mainform,name='mainform'),
    path('fs',fs,name='fs'),
    # path('fs',views.fs.as_view)
    path('stdhome',stdhome,name='stdhome'),
    path('stdreg',stdreg,name='stdreg')
    ,path('writestudent',writestudent,name='writestudent'),
    path('slogin',slogin,name='slogin'),
    path('s_cource_feedb',s_cource_feedb,name='s_cource_feedb'),
    path('up_st_fee_co',up_st_fee_co,name='up_st_fee_co'),
    path('s_faculty_feedb',s_faculty_feedb,name='s_faculty_feedb'),
]