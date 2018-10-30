from django import forms
from .models import MyAdminPanel


class AdminModelForm(forms.ModelForm):
    class Meta:
        model = MyAdminPanel
        fields = ('model_name', 'app_name',)
