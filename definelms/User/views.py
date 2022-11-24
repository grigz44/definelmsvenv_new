from django.shortcuts import render

#################### home ###############
def temp(request):

    return render(request, 'User_UI/index.html')


############### all exam ###################


def vexam(request):

    return render(request, 'User_UI/viewallexam.html')