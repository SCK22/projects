from django.urls import path
from .text import views as textviews
from .onlinemodel import views as onlinemodelviews
app_name = "api"

urlpatterns = [
    path("status",textviews.alive, name = "home"),
    path("tokenize",textviews.tokenize, name = "tokenize"),
    path("pos",textviews.get_pos_tags, name = "pos"),
    path("ner",textviews.get_ner_tags, name = "ner"),
    path("wv",textviews.get_word_vector, name = "wv"),
    path("similarity",textviews.get_word_similarity, name = "similarity"),
    path("onlinemodelstatus",onlinemodelviews.alive, name = "onlinemodelstatus"),
    path("testEvent", onlinemodelviews.success_on_event_receive, name = "testEvent"),
    path("receiveEvents", onlinemodelviews.save_event_received, name = "receiveEvents"),
    path("getData", onlinemodelviews.get_data, name = "getData"),
    path("getMeans", onlinemodelviews.get_means, name = "getMeans"),
    
]

