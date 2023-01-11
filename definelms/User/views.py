from django.shortcuts import render,redirect
from requests import post
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

def error404(request):

    return render(request, 'User_UI/404.html')


################ video class ############################



def vclass(request,id):

        st = video_class.objects.filter(course=id)
      
        context = {
            'vde':st
        }
        return render(request, 'User_UI/tutorials.html',context)


from django.shortcuts import render, get_object_or_404

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse



def home(request):
    if 'username' not in request.session:
        return redirect('login')
    else:
    
        form = CommentForm()
        dsn = videocomment.objects.all()
        
        context = {'form':form, 'dsn':dsn}
        return render(request, 'User_UI/comment.html', context)


@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cid = request.POST.get('dsnid')
            designation1 = request.POST['comment']
            designation1 = request.POST['comment']
            print('student id',cid)

            if(cid == ''):
                d = videocomment(comment=designation1)
            else:
                d = videocomment(id=cid, comment=designation1)
            d.save()

            dsn = videocomment.objects.values()
            student_data = list(dsn)
            return JsonResponse({'status':'Data Saved', 'student_data':student_data})
        else:
            return JsonResponse({'status':'Not Saved'})    

@csrf_exempt
def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('did')
        d = videocomment.objects.get(pk=id)
        d.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})    


@csrf_exempt
def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('did')
        print('Student ID',id)
        desgn = videocomment.objects.get(pk=id)
        student_data = {'id':desgn.id, 'comment':desgn.comment}
        return JsonResponse(student_data)




###################### comment ############################

def add_comment(request):
    if request.method == 'GET':
        video_id = request.GET['video_id']
        comment = request.GET['comment_text']
        video_obj = video_class.objects.get(id=video_id)
        session_obj = login.objects.get(username=request.user.username)
        video_comments = videocomment.objects.filter(post=video_obj).order_by('-id')
        create_comment = videocomment.objects.create(post=video_obj, user=session_obj, comment=comment)
        create_comment.save()

    return JsonResponse({'comment':create_comment.comment, 'count_comments':video_comments.count()})