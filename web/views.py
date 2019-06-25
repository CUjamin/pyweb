from django.shortcuts import render
from django.http import JsonResponse,request
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def nextflownode(request):
    if request.method=='GET':
        print("GET")
    # request.GET
    # nlpResponse=NlpReponse('tesk_1','call_2','123456',1,"SUCCESS")
        return JsonResponse({"result":0,"msg":"OK"})
    elif request.method=='POST':
        print("POST")
        return JsonResponse({"result": 1, "msg": "OK"})