from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User

from .models import *

def beforehome(request):
    return render(request, 'piroquiz/beforehome.html')

# Create your views here.
def CreateQuiz(request):
    #user = request.user

    if request.method == 'POST':
        title = request.POST.get('title')
        schoolans = request.POST.get('school')
        foodans = request.POST.get('food')
        answer = Answer.objects.create(
            title=title,
            schoolans=schoolans,
            foodans=foodans,
        )

        # user.answer = answer
        # user.save()

        url = reverse('piroquiz:index')
        return redirect(to=url)

    return render(request, 'piroquiz/createQuiz.html')

def index(request):
    qs = Answer.objects.all()

    return render(request,'piroquiz/index.html', {'lists': qs})

def DetailQuiz(request):
    return render(request,'piroquiz/detailQuiz.html')


def SolveQuiz(request, pk):
    # challenger = get_object_or_404(Challenger, pk=pk)
    # user = challenger.user_obj

    if request.method == 'POST':
        schoolans = request.POST.get('school')
        foodans = request.POST.get('food')
        correct = Correct.objects.create(
            schoolans=schoolans,
            foodans=foodans,
        )

        # challenger.result = correct
        # challenger.save()
        #
        # for i in range(2):
        #     if user.answer[1] == challenger.result[i]:
        #         print("match")


        url = reverse('piroquiz:index')
        return redirect(to=url)
    answer = Answer.objects.get(pk=pk)
    return render(request,'piroquiz/SolveQuiz.html', {'answer': answer})

def DeleteQuiz(request, pk):
    answer = Answer.objects.get(pk=pk)
    answer.delete()
    return redirect(reverse('piroquiz:index'))