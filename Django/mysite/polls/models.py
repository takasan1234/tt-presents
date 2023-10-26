from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 質問の内容
    pub_date = models.DateTimeField("date published")  # 作成日時


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # どの質問に対する回答か
    choice_text = models.CharField(max_length=200)  # 回答の選択肢
    votes = models.IntegerField(default=0)  # 投票数
    

class Sum(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    sum_votes = models.IntegerField(default=0) # 合計人数

# 未完成