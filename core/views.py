from django.shortcuts import render
from .dialogflow_client import get_chatbot_reply
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import DummyProperty


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
