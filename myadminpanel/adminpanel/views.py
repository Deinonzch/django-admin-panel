from django.shortcuts import render
from .models import MyAdminPanel
from .forms import AdminModelForm
from django.urls import reverse_lazy
from django.db import connection
from django.views import generic
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin


@permission_required('adminpanel.can_view')
def index(request):
    app_list = MyAdminPanel.objects.values('app_name').distinct()
    model_list = MyAdminPanel.objects.order_by('app_name')
    context = {'model_list': model_list, 'app_list': app_list}
    return render(request, 'adminpanel/index.html', context)


@permission_required('adminpanel.can_add')
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


class ModelView(PermissionRequiredMixin, generic.ListView):
    model = MyAdminPanel
    template_name = 'adminpanel/view_model.html'
    context_object_name = 'objects_list'
    permission_required = 'polls.can_view'

    def get_queryset(self, *args, **kwargs):
        return self.model.get_model(self.kwargs.get('app_name'), self.kwargs.get('model_name')).objects.order_by('pk')

    def get_context_data(self, **kwargs):
        context = super(ModelView, self).get_context_data(**kwargs)
        context['objects_list'] = self.model.get_model(self.kwargs.get('app_name'), self.kwargs.get('model_name')).objects.order_by('pk')
        context['model_id'] = self.kwargs.get('pk')
        context['model_name'] = self.kwargs.get('model_name')
        context['model_app'] = self.kwargs.get('app_name')
        print(self.kwargs.get('app_name'))
        return context


class CreateObjectView(PermissionRequiredMixin, generic.CreateView):
    model = MyAdminPanel
    fields = '__all__'
    template_name = 'adminpanel/createview_model.html'
    permission_required = 'polls.can_create_object'

    def get_form(self, form_class=None, **kwargs):
        self.model = self.model.get_model(self.kwargs.get('app_name'), self.kwargs.get('model_name'))
        form = super(CreateObjectView, self).get_form(form_class)  # instantiate using parent
        form.fields.queryset = self.model.objects.all()
        return form


class UpdateObjectView(PermissionRequiredMixin, generic.UpdateView):
    model = MyAdminPanel
    fields = '__all__'
    template_name = 'adminpanel/updateview_model.html'
    permission_required = 'polls.can_update_object'

    def get_form(self, form_class=None, **kwargs):
        self.model = self.model.get_model(self.kwargs.get('app_name'), self.kwargs.get('model_name'))
        form = super(UpdateObjectView, self).get_form(form_class)  # instantiate using parent
        form.fields.queryset = self.model.objects.all()
        return form

    def get_context_data(self, **kwargs):
        context = super(UpdateObjectView, self).get_context_data(**kwargs)
        context['object'] = self.model.objects.filter(id=self.kwargs.get('object_id'))
        context['model_id'] = self.kwargs.get('pk')
        context['model_name'] = self.kwargs.get('model_name')
        context['model_app'] = self.kwargs.get('app_name')
        print(self.kwargs.get('object_id'))
        return context

    def get_object(self, queryset=None, **kwargs):
        print(self.model.objects.get(id=self.kwargs['pk']))
        obj = self.model.objects.get(id=self.kwargs['pk'])
        return obj



class DeleteObjectView(PermissionRequiredMixin, generic.DeleteView):
    model = MyAdminPanel
    fields = '__all__'
    template_name = 'adminpanel/deleteview_model.html'
    success_url = reverse_lazy('list')
    permission_required = 'polls.can_delete_object'

    def get_context_data(self, **kwargs):
        context = super(DeleteObjectView, self).get_context_data(**kwargs)
        context['object'] = self.model.get_model(self.kwargs.get('app_name'), self.kwargs.get('model_name'))\
            .objects.filtr(id=self.kwargs.get('object_id'))
        context['model_id'] = self.kwargs.get('pk')
        context['model_name'] = self.kwargs.get('model_name')
        context['model_app'] = self.kwargs.get('app_name')
        print(self.kwargs)
        print('sgadgrgdvzd')
        return context
