from django.shortcuts import render
from pymongo import MongoClient
from pymongo import ReturnDocument
import json
from django.http import JsonResponse
from bson.json_util import dumps, loads

# Create your views here.


def home(request):
    return render(
        request,
        'restapi/home.html'
    )


def api_documents(request, document_type):
    server = 'localhost'
    port = 27017
    database = "marvel_restapi"

    collection = document_type

    client = MongoClient(server, port)
    db = client[database]
    data = db[collection]

    if request.method == 'GET':
        if request.body:
            get_data = json.loads(request.body)
            get_data = get_data["fields"]
        else:
            results = data.find()
            results = [doc for doc in results]
            results = dumps(results)
            return JsonResponse(results, safe=False)

        return api_get(data, 0, get_data)

    if request.method == 'POST':
        post_data = json.loads(request.body)
        post_data = post_data["fields"]
        return api_post(data, post_data)

    if request.method.lower() == 'delete':
        delete_ids = json.loads(request.body)
        if delete_ids:
            delete_ids = delete_ids["fields"]
        else:
            return JsonResponse({
                "Message":
                "Error: no body data to enter"
            })
        return api_delete(data, 0, delete_ids)

    if request.method == 'PUT':
        put_data = json.loads(request.body)
        put_data = put_data["fields"]
        return(api_put(data, put_data))


def api_document_type(request, document_type, document_id):
    server = 'localhost'
    port = 27017
    database = "marvel_restapi"

    collection = document_type

    client = MongoClient(server, port)
    db = client[database]
    data = db[collection]

    if request.method == 'GET':
        get_data = json.loads(request.body)
        if get_data:
            get_data = get_data["fields"]
        else:
            get_data = 0
        return api_get(data, document_id, get_data)

    if request.method == 'POST':
        post_data = json.loads(request.body)
        post_data = post_data["fields"]
        return api_post(data, post_data)

    if request.method == '\DELETE':
        delete_ids = json.loads(request.body)
        if delete_ids:
            delete_ids = delete_ids["fields"]
        else:
            delete_ids = 0
        return api_delete(data, document_id, delete_ids)

    if request.method == 'PUT':
        put_data = json.loads(request.body)
        put_data = put_data["fields"]
        return(api_put(data, put_data))


def api_get(data, document_id, get_data):
    data_retrieve = []
    if get_data:
        for item in get_data:
            data_retrieve.append(data.find_one({'id': item["id"]}))
    else:
        data_retrieve.append(data.find_one({'id': document_id}))
    data_retrieve = dumps(data_retrieve)
    return JsonResponse(data_retrieve, safe=False)


def api_post(data, post_data):
    results_json = data.insert_many(post_data)
    results_json = dumps(results_json.inserted_ids)
    results_json += (" successfully added")
    return JsonResponse(results_json, safe=False)


def api_delete(data, document_id, delete_ids):
    if delete_ids:
        results_json = []
        for item in delete_ids:
            try:
                results = data.delete_one(
                    {"id": item["id"]}
                )
            except:
                print("deletion error")
            results_json.append(
                "Deletion count: " + str(results.deleted_count)
            )
    else:
        results = data.deleteOne(
            {"id": document_id}
        )
        results_json.append(results)

    results_json = dumps(results_json)
    return JsonResponse(results_json, safe=False)


def api_put(data, put_data):
    results_json = []
    for item in put_data:
        put_request = {}
        for key in item:
            put_request.update({
                key: item[key]
            })

        results = data.update(
            {"id": item["id"]},
            {'$set': put_request},
            upsert=True)
        results_json.append(results)

    results_json = dumps(results_json)
    return JsonResponse(results_json, safe=False)
