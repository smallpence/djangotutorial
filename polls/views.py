"layout of the polls app"

from django.http import HttpResponse

def index(_):
    "/"
    return HttpResponse("Hello world from polls!")
