from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chat(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message", "")

        reply = "You said: " + message

        return JsonResponse({"response": reply})

    return JsonResponse({"message": "Send POST request"})