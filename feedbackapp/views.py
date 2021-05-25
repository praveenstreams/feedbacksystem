from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from feedbackapp.models import faculty,facultyfeedback

def home(request):
    return render(request,'apphome.html')
def facultyhome(request):
    return  render(request,'facultyhome.html')


def registerform(request):
    return render(request,'registerform.html')

def writefaculty(request):
    name=request.GET['regname']
    number=request.GET['mob']
    passw=request.GET['pass']
    cpass=request.GET['cpass']

    if len(name)==0 or len(number)==0 or len(passw)==0 or len(cpass)==0 or passw !=cpass or len(number)<10:
        txt="NOT VALID"

    else:

        value=faculty(name=name,number=number,password=passw)
        value.save()
        txt="SUCCESSFULLY REGISTERED LOGIN"

    return render(request, 'registerform.html', {"txt": txt})


def flogin(request):
    number=request.GET['num']
    password=request.GET['password']


    if len(number) ==0 or len(password)==0:
        txt="FILL THE FIELDS"
        return render(request,'facultyhome.html',{"txt":txt})


    else:
        data=faculty.objects.filter(number=number,password=password).values()
        if len(data)==0:
            txt="invalid number/password"
            return render(request,'facultyhome.html',{"txt":txt})


        else:
            #[{'id': 1, 'name': 'praveen kumar', 'number': 8714249383,   'password': 'password'}]

            global nme


            nme=data[0]["name"]


            print("/////////////////////////////////////////////////////",nme)


            return  render(request,'mainform.html')


def mainform(request):


    global nme


    course=request.GET['course']
    if len(course)==0:
        txt="FILL ALL THE FIELDS"
        return HttpResponse(txt)
    else:


        department=request.GET['department']
        try:
            check=request.GET['check']
        except:
            check=0
        try:
            check2=request.GET['check2']
        except:
            check2=0

        try:
            check3=request.GET['check3']
        except:
            check3=0

        try:
            check4=request.GET['check4']
        except:
            check4=0

        try:
            check5=request.GET['check5']
        except:
            check5=0

        try:
            check6=request.GET['check6']
        except:
            check6=0


        try:
            check7=request.GET['check7']
        except:
            check7=0

        try:
            check8=request.GET['check8']
        except:
            check8=0
        try:
            check9=request.GET['check9']
        except:
            check9=0

        try:
            check10=request.GET['check10']
        except:
            check10=0

        try:
            check11=request.GET['check11']
        except:
            check11=0


        try:
            check12=request.GET['check12']
        except:
            check12=0

        try:
            check13=request.GET['check13']
        except:
            check13=0
        try:
            check14=request.GET['check14']
        except:
            check14=0

        try:
            check15=request.GET['check15']
        except:
            check15=0

        try:
            check16=request.GET['check16']
        except:
            check16=0

        try:
            check17=request.GET['check17']
        except:
            check17=0


        value=facultyfeedback(name=nme,department=department,course=course,adequacy_of_ourse_sylabus=check,Background_for_benefiting_courcr=check2,course_difficulty_to_understand=check3,syllabus_completeing_range=check4,library_material_availability=check5,difficulty_to_get_material=check6,levelof_preparation_for_class=check7,how_teacher_able_to_communicate=check8,how_teacher_encourages_student=check9,method_of_encouraging=check10,how_helps_advicing=check11,teachers_approach=check12,Internal_assessment=check13,effect_of_internal_assesment=check14,how_often_gets_feedback_on_performance=check15,Were_your_assignments_discussed_with_you=check16,Were_you_provided_with_course_contributory_lecture_too_at_the_beginning=check17)
        value.save()
        print(course,department,check,check2,check3,check4,check5,check6,check7,check8,check9,check10,check11,check12,check13,check14,check15,check16,check17)

        return HttpResponse("UPLOADED")




def fs(reuest):


    global nme


    value=facultyfeedback.objects.filter(name=nme)

    print(value,"/////////////////////////////////////")
    print(nme)

    rows=len(value)

    if rows==0:
        return HttpResponse("NO ACTIVITY FOUND")

    else:
        sh=[]

        for i in range(rows):
            sh.append(("You were leave the feedback on course : "+value[i].course))

        return render(reuest,'activities.html',{"data":sh})


# text-align: right;
