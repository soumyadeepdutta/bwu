from django.shortcuts import render
from .dialogflow_client import get_chatbot_reply
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import DummyProperty
import json
from .save_user import *

def home(request):
    dummydata = DummyProperty.objects.all()
    return render(request, 'core/base.html', {'object_list': dummydata})


@csrf_exempt
def webhook(request):
    if request.method == "POST":
        query = request.POST.get('query')
        reply = get_chatbot_reply(query)
        # print(reply)
        return JsonResponse({'reply': reply})
        # return HttpResponse('')

@csrf_exempt
def save(request):
    if request.method == 'POST':
        req = json.loads(request.body.decode('utf-8'))
        action = req.get('queryResult').get('action')
        context = dict(req.get('queryResult').get('outputContexts')[0])
        if action == 'find_home.find_home-yes':
            params = context['parameters']
            createUser(params)

    return JsonResponse({'error' : 'GET Request not accepted'})