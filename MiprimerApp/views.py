from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse

# Create your views here.

def HolaMundo(request):
    return HttpResponse("Hola Mundo")

def acerca(request):
    return HttpResponse("<h1> NO mames es acerca de la vaina </h1>")

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #latest_question_list = Question.objects.all()
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'MiprimerApp/index.html', context)
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'MiprimerApp/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'MiprimerApp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('miprimerapp:results', args=(question.id,)))

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'MiprimerApp/detail.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'MiprimerApp/detail.html', {'question': question})

