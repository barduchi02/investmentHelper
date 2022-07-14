import datetime

from django import forms

from .models import Tunnel, Asset


class TunnelForm(forms.ModelForm):
    assetid = forms.ModelChoiceField(queryset=Asset.objects.all(), empty_label='Selecionar Ativo', label='Ativo')
    period = forms.TimeField(label='Perído de atualização',
                             error_messages={'invalid': 'Por favor, entre com um período de tempo válido (HH:mm)'})
    min_price = forms.FloatField(label='Preço mínimo', min_value=0)
    max_price = forms.FloatField(label='Preço máximo', min_value=0)

    def __init__(self, *args, **kwargs):
        super(TunnelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['required'] = ''
            visible.field.widget.attrs['placeholder'] = visible.field.label

            if visible.field.label.startswith('Preço'):
                visible.field.widget.attrs['step'] = '0.01'

    class Meta:
        model = Tunnel
        fields = ['assetid', 'period', 'min_price', 'max_price']

    def clean(self):
        cleaned_data = super(TunnelForm, self).clean()

        if cleaned_data['max_price'] <= cleaned_data['min_price']:
            self.add_error('max_price', 'O Preço máximo deve ser maior que o mínimo.')

        if cleaned_data['period'] == datetime.time.min:
            self.add_error('period', 'O Período deve ser maior do que zero.')
