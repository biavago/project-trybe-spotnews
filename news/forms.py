from django import forms


class CategoriesForms(forms.Form):
    name = forms.CharField(max_length=200, label="Nome")
