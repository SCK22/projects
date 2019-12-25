from django.urls import path
from .text import views


app_name = "api"

urlpatterns = [
    path("status",views.alive, name = "home"),
    path("tokenize",views.tokenize, name = "tokenize"),
    path("pos",views.get_pos_tags, name = "pos"),
    path("ner",views.get_ner_tags, name = "ner"),
    path("wv",views.get_word_vector, name = "wv"),
    path("similarity",views.get_word_similarity, name = "similarity"),
    
]

