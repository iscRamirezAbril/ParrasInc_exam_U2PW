from multiprocessing import context
from urllib import response
from django.shortcuts import render

# |-----| All the necessary Libs |-----|
from rest_framework.response import Response
from rest_framework.decorators import api_view

# |-----| Views |-----|
@ api_view(['GET'])
def getAssistenceList(request):
    context = {'name': 'Abril', 'age': 21}
    return response(context)
