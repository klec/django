import logging
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    soap_request_data = request.body

    # Залогируйте данные SOAP-запроса
    logger.info('Received SOAP request: %s', soap_request_data)
    return HttpResponse("Hello, world. You're at the polls index.")