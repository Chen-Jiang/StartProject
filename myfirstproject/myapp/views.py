from django.shortcuts import render
from . import models
from django.http import JsonResponse
from django.core import serializers
import json


# Create your views here.

def add_book(request):
    response = {}

    try:
        book = models.Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 0

    return JsonResponse(response)


def show_books(request):
    response = {}

    try:
        books = models.Book.objects.filter()
        response['list'] = json.loads(serializers.serialize('json', books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

