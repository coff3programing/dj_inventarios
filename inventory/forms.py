from django import forms
from .models import (
    LaboratoriosModel,
    MarcasModel,
    TipoActivosModel,
    ActivosModel
)


class LaboratoriosForm(forms.ModelForm):
    class Meta:
        model = LaboratoriosModel
        fields = '__all__'


class MarcasForm(forms.ModelForm):
    class Meta:
        model = MarcasModel
        fields = '__all__'


class TipoActivosForm(forms.ModelForm):
    class Meta:
        model = TipoActivosModel
        fields = '__all__'


class ActivosForm(forms.ModelForm):
    class Meta:
        model = ActivosModel
        fields = '__all__'
        widgets = {
            'laboratorio': forms.Select(attrs={'class': 'form-select'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'marca': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'estado_uso': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['laboratorio'].queryset = LaboratoriosModel.objects.all()
        self.fields['tipo'].queryset = TipoActivosModel.objects.all()
        self.fields['marca'].queryset = MarcasModel.objects.all()
