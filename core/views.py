from django.shortcuts import render
from .dialogflow_client import get_chatbot_reply
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def home(request):
    return render(request, 'core/base.html')


@csrf_exempt
def webhook(request):
    if request.method == "POST":
        query = request.POST.get('query')
        reply = get_chatbot_reply(query)
        # print(reply)
        return JsonResponse({'reply': reply})
        # return HttpResponse('')
