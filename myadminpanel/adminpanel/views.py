from django.shortcuts import render
from .models import MyAdminPanel
from django.http import HttpResponse
from django.template import loader


def index(request):
    model_list = MyAdminPanel.objects.order_by('-model_name')
    template = loader.get_template('adminpanel/index.html')
    context = {
        'model_list': model_list,
    }
    return HttpResponse(template.render(context, request))


def add_model(request):
    pass
