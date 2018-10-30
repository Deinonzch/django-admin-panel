from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import MyAdminPanel
from .forms import AdminModelForm
from django.urls import reverse
from django.db import connection
from django.views import generic
from django.apps import apps


def index(request):
    app_list = MyAdminPanel.objects.values('app_name').distinct()
    model_list = MyAdminPanel.objects.order_by('app_name')
    context = {'model_list': model_list, 'app_list': app_list}
    return render(request, 'adminpanel/index.html', context)


def add_model(request):
    form = AdminModelForm()
    if request.method == 'POST':
        form = AdminModelForm(request.POST)
        if form.is_valid():
            name_model = form.cleaned_data['model_name']
            name_app = form.cleaned_data['app_name']
            if not MyAdminPanel.objects.filter(model_name=name_model.lower(), app_name=name_app.lower()).first():
                table_name = str(name_app).lower() + '_' + str(name_model).lower()
                result = table_name in connection.introspection.table_names()
                if result:
                    form.save(commit=True)
                    return index(request)
                else:
                    print("Don't exist in DB")
            else:
                print("Exist in MyAdminPanel")
        else:
            print(form.errors)

    return render(request, 'adminpanel/add_model.html', {'form': form})


class ModelView(generic.ListView):
    model = MyAdminPanel
    template_name = 'adminpanel/view_model.html'
    context_object_name = 'objects_list'

    def get_queryset(self, *args, **kwargs):
        return self.model.get_model(self.kwargs.get('app_name'), self.kwargs.get('model_name')).objects.order_by('pk')
