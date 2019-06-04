from django.shortcuts import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# from web.models import NlpReponse

@api_view(['GET'])
def getnextflownode(request,*args):
    if request
    # request.GET
    # nlpResponse=NlpReponse('tesk_1','call_2','123456',1,"SUCCESS")
    return JsonResponse({"result":0,"msg":"OK"})




