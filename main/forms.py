from django import forms
from .models import Films


class FilmsCreateForm(forms.ModelForm):
    class Meta:
        model = Films
        fields = 'image name producer rating duration genre'.split()
        widgets = {
            'image': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'file'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'producer': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'rating': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'duration': forms.TimeInput(attrs={
                'class': 'form-control'
            }),
            'genre': forms.Select(attrs={
                'class': 'form-control'
            })
        }
