from django.shortcuts import render
from django.http import HttpResponse
from studentfeedbackapp.models import  student
# Create your views here.
from sqlalchemy.testing.provision import register
def stdhome(request):
    return render(request,'studentlogin.html')
def stdreg(request):
    return render(request,'studentregister.html')
def writestudent(request):
    name = request.GET['regname']
    number = request.GET['mob']
    passw = request.GET['pass']
    cpass = request.GET['cpass']
    if len(name) == 0 or len(number) == 0 or len(passw) == 0 or len(cpass) == 0 or passw != cpass or len(number) < 10:
        txt = "NOT VALID"
    else:
        value = student(name=name, number=number, password=passw)
        value.save()
        txt = "SUCCESSFULLY REGISTERED LOGIN"
    return render(request, 'studentregister.html', {"txt": txt})
def slogin(request):

    number = request.GET['num']
    password = request.GET['password']
    if len(number) == 0 or len(password) == 0:
        txt = "FILL THE FIELDS"
        return render(request, 'studentlogin.html', {"txt": txt})
    else:
        data = student.objects.filter(number=number, password=password).values()
        if len(data) == 0:
            txt = "invalid number/password"
            return render(request, 'studentlogin.html', {"txt": txt})
        else:
            # [{'id': 1, 'name': 'praveen kumar', 'number': 8714249383,   'password': 'password'}]
            global nme
            nme = data[0]["name"]
            print("/////////////////////////////////////////////////////", nme)
            return render(request, 'selection.html')


def s_cource_feedb(request):
    return render(request,"s_course.html")

def up_st_fee_co(request):
    department=request.GET['department']
    sem=request.GET['sem']
    content=request.GET['content']
    coverage=request.GET['coverage']
    application=request.GET['application']
    value=request.GET['value']
    clarity=request.GET['clarity']
    metirial=request.GET['metirial']
    effort=request.GET['effort']
    overall=request.GET.get('overall')

    print(department,sem,content,coverage,application,value,clarity,metirial,effort,overall)



    return HttpResponse(department)


def s_faculty_feedb(request):
    return render(request,"s_faculty_feedb.html")












# input[type=radio] {
#     border: 0px;
#     width: 100%;
#     height: 3em;
# }

