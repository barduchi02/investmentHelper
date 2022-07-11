from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('investmentApp/index.html')
    context = {
        'teste': "Hello, world. You're at the polls index.",
    }
    return HttpResponse(template.render(context, request))
