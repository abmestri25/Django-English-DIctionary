from django import forms


class MeaniningForm(forms.Form):
    word = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Here..'}))
