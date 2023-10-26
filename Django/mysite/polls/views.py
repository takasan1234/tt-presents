# 添削済みーーーーーーーーーーーーーーーーーーー

from django.http import Http404, HttpResponse

from .models import Question,Choice,Sum
from django.shortcuts import get_object_or_404, render, redirect  # get_object_or_404 を追加

def index(request):
    # 新しいものから 5 個
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)



#   get_object_or_404(クラス名, 引数)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question,
    }
    return render(request, "polls/detail.html", context)



# results関数
# pkの番号に相当する質問を、results.htmlのquestionに代入する関数

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    sum_votes = get_object_or_404(Sum, pk=1) 
    context = {
        "question" : question,
    }
    return render(request, "polls/results.html", context)



# vote関数



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    sum_votes = get_object_or_404(Sum, pk=1)  # Sumモデルから合計投票数を取得

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice."
        })
    else:
        sum_votes.sum_votes += 1  # 合計投票数を更新
        sum_votes.save()
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('polls:results', question.id)

        # わからんーーーーーーーーーーーーーーーーーー

def resets(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    sum_votes = get_object_or_404(Sum, pk=1)
    choices_to_reset = request.POST.getlist("resets")
    for choice_id in choices_to_reset:
        choice = get_object_or_404(Choice, pk=choice_id)
        sum_votes.sum_votes = sum_votes.sum_votes - choice.votes # 合計投票数を更新
        sum_votes.save()
        choice.votes = 0
        choice.save()
        # POST データを正常に処理した後は、redirect() を返します。これにより、ユーザーが「戻る」ボタンを押した場合にデータが 2 回投稿されるのを防ぎます。
    return redirect('polls:results', question_id)


# 変更した
# forresetsビューの修正
def forresets(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/forresets.html", {"question": question})



