from django.shortcuts import render,redirect
from lmsmainapp.forms import *
from lmsmainapp.models import *

#################### home ###############
def temp(request):

    return render(request, 'User_UI/index.html')

def about(request):

    return render(request, 'User_UI/about.html')


def contact(request):

    return render(request, 'User_UI/contact.html')

############### all exam ###################


def vexam(request):
        exm = exam.objects.all()
        context = {'exm':exm}
        return render(request, 'User_UI/viewallexam.html', context)


############### all Courses ###################


def vcourse(request):
        cr = course.objects.all()
        context = {
            'cr':cr
            }
        return render(request, 'User_UI/allcourse.html',context)