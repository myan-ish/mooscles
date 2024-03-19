from django.http.response import HttpResponse

from core.utils import info_logger

def login(request):
    info_logger(request.request_id, "Testing log")
    return HttpResponse("S")