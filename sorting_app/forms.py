from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['file', 'algorithm_type']

        widgets = {'file': forms.FileInput(attrs={
            'class': 'form-control',
            'type': 'file',
        }),
            'algorithm_type': forms.Select(attrs={
                'class': 'form-select',
            })
        }


class GenerateForm(forms.Form):
    title = forms.CharField(
        max_length=15,
        label='Input filename',
        widget=forms.TextInput(attrs={
            'class': 'form-control mb-2',
            'placeholder': 'Введите имя файла'
        })
    )
    quantity = forms.IntegerField(
        max_value=1000,
        label='Enter the number of values',
        widget=forms.NumberInput(attrs={
            'class': 'form-control mb-5',
            'placeholder': 'Введите количество значений',
        })
    )
