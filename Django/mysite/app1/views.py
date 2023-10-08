from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# 以下はpollsのためのコード

# from .models import Question
# from django.http import Http404

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     context = {
#         "question": question,
#     }
#     return render(request, "polls/detail.html", context)
#     return HttpResponse("You're looking at question %s." % question_id)


# def results(request, question_id):
#     return HttpResponse("You're looking at the results of question %s." % question_id)


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)


# def index(request):
#     # 新しいものから 5 個
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return render(request, "polls/index.html", context)



# 以下は申込フォームのためのコード
from app1.forms import ContactForm
from django.shortcuts import redirect
from django.utils import timezone
import logging

# logging.basicConfig(filename='/srv/backend/view/logs/example.log',level=logging.DEBUG)
# logging.debug('This message should go to the log file')

# Create your views here.
def contact(request):
    logging.debug('Hello World!')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        logging.debug(form)

        if form.is_valid():
            post = form.save(commit=False)
            post.contact_time = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'form.html', {'form': form})

def index(request):
    return HttpResponse("index Page")

def homepage(request):
    return render(request, 'index.html', {'index': index})