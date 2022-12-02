from django.shortcuts import render,redirect
from lmsmainapp.forms import *
from lmsmainapp.models import *


############### login #################

def login(request):

    return render(request, 'User_UI/login.html')
  
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


def vcourse(request,id):

        exm = course.objects.filter(exam=id)
      
        context = {
            'exm':exm
        }
        return render(request, 'User_UI/allcourse.html',context)



################### video tutorials #########################




# def tutorial(request):

#     return render(request, 'User_UI/tutorials.html')




def error404(request):

    return render(request, 'User_UI/404.html')


################ video class ############################



def vclass(request,id):

        st = video_class.objects.filter(course=id)
      
        context = {
            'vde':st
        }
        return render(request, 'User_UI/tutorials.html',context)








