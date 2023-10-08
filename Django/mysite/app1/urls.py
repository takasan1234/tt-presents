from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/


    # 以下2行
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("homepage/", views.homepage, name="hoempage"),
    


    
    
    # ex: /polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]