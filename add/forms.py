from django import forms
from django.forms import ModelForm
from .models import Advert
# class AdvertForm(forms.Form):
#     title = forms.CharField(max_length=64, widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
#     price = forms.DecimalField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
#     auction = forms.BooleanField(required=False)
#     image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))

class AdvertForm(ModelForm):
    
    class Meta:
        model = Advert
        fields = ['title', 'description', 'price', 'auction', 'image']
        
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control form-control-lg form-group row',
                                             'self-align' : 'center'}),
            'description' : forms.Textarea(attrs={'class' :'form-control form-control-lg form-group row'}),
            'price' : forms.NumberInput(attrs={'class' :'form-control form-control-lg form-group row'}),
            'auction' : forms.CheckboxInput(attrs={'class' : 'form-check-input '}),
            'image' : forms.FileInput(attrs={'class' : 'form-control form-control-lg '})
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not '?' in title:
            return title 
        else:
            raise forms.ValidationError(
            ('Invalid value: %(value)s'),
            code='invalid',
            params={'value' : 'В заголовке присутсвует "?"'}
        )
        
    #     widgets = {
    #         'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
    #         'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
    #         'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
    #         'auction': forms.CheckboxInput(),
    #         'image': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg'})
    #     }