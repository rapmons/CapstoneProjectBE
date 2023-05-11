from django.urls import path
from .Views.users import RegisterView, LoginView, UserView, LogoutView
from .Views.detect import createHistoryWordsView
from .Views.words import Command
from .Views.myWords import saveWordsView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path("detect",createHistoryWordsView.as_view()),
    path("words",Command.as_view()),
    path("save-my-word",saveWordsView.as_view())
]
