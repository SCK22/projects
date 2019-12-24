import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from nltk.tokenize import word_tokenize
from django.http import HttpResponseForbidden

import spacy
nlp = spacy.load("en_core_web_md")

def cannot_handle_request(r):
    return HttpResponseForbidden(content="Request type {} not supported".format(r.method))

def alive(request):
    return HttpResponse("I am Alive!", status= 200)

def tokenize(request):
    if request.method == "POST":
        text = json.loads(request.body)["text"]
        print("body", text, flush = True)
        doc = nlp(json.loads(request.body)['text'])
        tokens = [token.text for token in doc]
        return JsonResponse(status= 200, data = {"text" : text, "tokens" : tokens})
    else:
        return cannot_handle_request(request)
        
def get_pos_tags(request):
    if request.method == "POST":
        text = json.loads(request.body)["text"]
        print("body", text, flush = True)
        doc = nlp(json.loads(request.body)['text'])
        pos_dict = {ent.text :ent.pos_ for ent in doc}
        return JsonResponse(status= 200, data = {"text" : text, "pos_dict" : pos_dict})
    else:
        return cannot_handle_request(request)

def get_ner_tags(request):
    if request.method == "POST":
        text = json.loads(request.body)["text"]
        print("body", text, flush = True)
        doc = nlp(json.loads(request.body)['text'])
        ner_dict = {ent.text :ent.label_ for ent in doc.ents}
        return JsonResponse(status= 200, data = {"text" : text, "ner_dict" : ner_dict})
    else:
        return cannot_handle_request(request)
            
def get_word_vector(request):
    if request.method == "POST":
        text = json.loads(request.body)["text"]
        print("body", text, flush = True)
        doc = nlp(json.loads(request.body)['text'])
        doc_text_vector_exists = {ent.text : str(ent.has_vector) for ent in doc.ents}
        doc_text_vector = {ent.text : str(ent.vector) for ent in doc.ents}
        doc_text_vector_norm = {ent.text : str(ent.vector_norm) for ent in doc.ents}
        print("doc_text_vector : {}".format(doc_text_vector))
        return JsonResponse(status= 200, data = {
                                                "text" : text, 
                                                "doc_text_vector_exists" : doc_text_vector_exists,
                                                "doc_text_vector" : doc_text_vector,
                                                "doc_text_vector_norm" : doc_text_vector_norm
                                                }
                            )
    else:
        return cannot_handle_request(request)


def get_word_vector(request):
    try:
        if request.method == "POST":
            text = json.loads(request.body)["text"]
            print("body", text, flush = True)
            doc = nlp(json.loads(request.body)['text'])
            doc_text_vector_exists = {ent.text : str(ent.has_vector) for ent in doc.ents}
            doc_text_vector = {ent.text : str(ent.vector) for ent in doc.ents}
            doc_text_vector_norm = {ent.text : str(ent.vector_norm) for ent in doc.ents}
            print("doc_text_vector : {}".format(doc_text_vector))
            return JsonResponse(status= 200, data = {
                                                    "text" : text, 
                                                    "doc_text_vector_exists" : doc_text_vector_exists,
                                                    "doc_text_vector" : doc_text_vector,
                                                    "doc_text_vector_norm" : doc_text_vector_norm
                                                    }
                                )
    except:
        return cannot_handle_request(request)

def get_word_similarity(request):
    # try:
        if request.method == "POST":
            text = json.loads(request.body)["text"]
            doc = nlp(json.loads(request.body)['text'])
            print("body", text, flush = True)
            similarity_dict = {}
            for token1 in doc:
                for token2 in doc:
                    if (token1.has_vector) and (token2.has_vector):
                        similarity_dict["{}_{}".format(token1.text,token2.text)] = str(token1.similarity(token2))
            print("body", text, flush = True)
            print("similarity_dict : {}".format(similarity_dict))
            # doc_text_vector_exists = {ent.text : str(ent.has_vector) for ent in doc.ents}
            # doc_text_vector = {ent.text : str(ent.vector) for ent in doc.ents}
            # doc_text_vector_norm = {ent.text : str(ent.vector_norm) for ent in doc.ents}
            print("similarity_dict : {}".format(similarity_dict))
            return JsonResponse(status= 200, data = {
                                                    "text" : text, 
                                                    "similarity_dict" : similarity_dict
                                                    }
                                )
    # except:
    #     return cannot_handle_request(request)