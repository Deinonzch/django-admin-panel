from django.shortcuts import render
from .models import MyAdminPanel


def index(request):
    model_list = MyAdminPanel.objects.order_by('-model_name')
    context = {'model_list': model_list}
    return render(request, 'adminpanel/index.html', context)


def add_model(request):
    pass
