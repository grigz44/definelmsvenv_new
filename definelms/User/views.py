from django.shortcuts import render
from lmsmainapp.forms import *
from lmsmainapp.models import *

#################### home ###############
def temp(request):

    return render(request, 'User_UI/index.html')


############### all exam ###################


def vexam(request):
    total_exam     = exam.objects.count()
    total_question = question_bank.objects.count()
    context={
        'exam'    :[total_exam,total_question,]
        
    }

    return render(request, 'User_UI/viewallexam.html',context)