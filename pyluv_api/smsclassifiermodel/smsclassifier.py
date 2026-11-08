from django.http import HttpResponse, HttpResponseBadRequest

from .classifier import classify


def classify_text(request):
    """GET /api/sms/id/classify?sms_text=<sms>  ->  "normal", "promo" or "spam"."""
    text = request.GET.get("sms_text")
    if not text:
        return HttpResponseBadRequest("Pass the SMS text as ?sms_text=...")
    return HttpResponse(classify(text), content_type="text/plain")
