from django.urls import path
from .Views.users import RegisterView, LoginView, UserView, LogoutView
from .Views.detect import createHistoryWordsView
from .Views.words import Command
from .Views.myWords import saveWordsView, GameView,WordSavedView
from .Views.topic import getResultWord, Game,getListWord
from .Views.historySearch import createView, historyView
from .Views.topic import saveResul
urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path("detect",createHistoryWordsView.as_view()),
    path("words",Command.as_view()),
    path("save-my-word",saveWordsView.as_view()),
    path("game",GameView.as_view()),
    path("list-word-detect",WordSavedView.as_view()),
    path("get-result",getResultWord.as_view()),
    path("game-toeic",Game.as_view()),
    path("get-list-word",getListWord.as_view()),
    path("create-search",createView.as_view()),
    path("get-list-history-search",historyView.as_view()),
    path("save-result", saveResul.as_view())
]
