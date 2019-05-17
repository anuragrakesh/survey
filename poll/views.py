from typing import Any, Iterator

from django.shortcuts import render, HttpResponseRedirect
from .models import Question
from .forms import regis_form
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = regis_form(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('farm.html')
    else:
        form = regis_form()
        return render(request, "register.html", {'form': form})


def farm(request):
    questions = Question.objects.all()
    n = len(questions)
    if request.method == 'POST':
        count = 0
        options = request.POST.dict()
        for q_id, option in options.items():
            if q_id != 'csrfmiddlewaretoken':
                q = Question.objects.get(id=q_id)
                # print(q_id, '=', option)
                if q.ans == option:
                    count = count + 1
        cou = {'count': count, 'range': range(1, n), 'question': questions, 'q_id': q_id, 'option': options}
        return render(request, 'performance.html', cou)
        # return options
    else:
        params = {'range': range(1, n), 'question': questions}
        return render(request, 'farm.html', params)


def performance(request):
    questions = Question.objects.all()
    n = len(questions)
    params = {'range': range(1, n), 'question': questions}
    return render(request, 'performance.html', params)
