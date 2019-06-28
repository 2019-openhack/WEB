from django import forms

class PDForm(forms.Form):
    pdf=forms.FileField()
