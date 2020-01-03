import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseForbidden
from .data_handling import dataHandler



def cannot_handle_request(r):
    return HttpResponseForbidden(content="Request type {} not supported".format(r.method))

def alive(request):
    return HttpResponse("Online model alive!", status= 200)

def success_on_event_receive(request):
    if request.method == "POST":
        record = json.loads(request.body)["data"]
        print("record", record)
        return JsonResponse(status= 200, data = {"record" : record, "status" : "Success!"})
    else:
        return cannot_handle_request(request)


def save_event_received(request):
    if request.method == "POST":
        record = json.loads(request.body)["data"]
        dataset = json.loads(request.body)["dataset"]
        print("record", record)
        data_handler = dataHandler(dataset)
        data_handler.save_records(record)
        return JsonResponse(status= 200, data = {"record" : record, "status" : "Success!"})
    else:
        return cannot_handle_request(request)

def get_data(request):
    if request.method == "GET":
        dataset = json.loads(request.body)["dataset"]
        data_handler = dataHandler(dataset)
        data,col_names  = data_handler.get_records()
        return JsonResponse(status= 200, data = {"data" : data, "col_names" : col_names, "status" : "Success!"})
    else:
        return cannot_handle_request(request)


def get_means(request):
    if request.method == "GET":
        dataset = json.loads(request.body)["dataset"]
        data_handler = dataHandler(dataset)
        data_dict  = data_handler.get_mean()
        return JsonResponse(status= 200, data = {"data" : data_dict, "status" : "Success!"})
    else:
        return cannot_handle_request(request)