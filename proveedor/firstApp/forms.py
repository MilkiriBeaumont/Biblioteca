from django import forms
from django import proyecto
class FormProyecto (forms.ModelForm):
    class meta:
        model = proyecto
        fields = '__all__'