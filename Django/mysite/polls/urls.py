
# 添削済み---------------------------------



from django.urls import path

from . import views

app_name = "polls"
# 他のアプリケーションのindex.htmlと区別


urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # path("ensyu<int:question_id>/", views.ensyu, name="ensyu"),
    path("<int:question_id>/forresets/",views.forresets, name="forresets"),
    path("<int:question_id>/resets/", views.resets, name="resets"),
]