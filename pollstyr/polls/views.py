
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib import messages
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import *


# get question and display.
def index(request):
    
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, 'index.html', context)
    

# show specific question and choices


def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExits:
        raise Http404("Question does not exits")
    return render(request, 'details.html', {'question': question})


# get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    return render(request, 'results.html', {'question': question})


def vote(request, question_id):

    # choice = get_object_or_404(Choice, pk=question_id)
    # if Vote.objects.filter(choice=choice,voter1=request.user).exists():
    #     messages.error(request,"Already Voted on this choice")
    #     return redirect('polls:index')
    # else:
    #     choice.votes += 1
    #     choice.save()
    #     Vote.objects.create(voter=request.user, choice=choice)
    #     return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
      

    question = get_object_or_404(Question, pk=question_id)
    
    
    if Vote.objects.filter(question=question,vote=request.user).exists():
        messages.error(request,"Already Voted on this Question")
        return redirect('polls:index')
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'details.html', {'question': question, 'error_message': "you did not select a choice", })
    
    else:
        
        selected_choice.votes += 1
        selected_choice.save()
        v= Vote(question=question,vote=request.user)
        v.save()
        
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))



def register(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password1 = request.POST['psw']
        password2 = request.POST['psw-repeat']
        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                return redirect('polls:register')
            else:
                user = User.objects.create_user(
                    username=user_name, password=password1)
                user.save()
                print('user created')
                return redirect('/')
        else:
            print("password not matching...")
            return redirect("polls:register")
        return redirect('/')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password1 = request.POST.get('psw')

        user = auth.authenticate(username=user_name, password=password1)
        if user is not None:
            auth.login(request, user)

            return redirect('polls:index')
        else:
            return redirect('polls:login')

    else:
        return render(request, 'login.html')


def pages(request):
    return render(request, 'pages.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def voter(request):
    voter= Vote.objects.all()
    return render(request,'showvoter.html',{'voter':voter})


