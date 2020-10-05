from django import forms

from .models import test


class Testform (forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"col-md4"}))
    userid=forms.IntegerField()
    class Meta:
        model=test
        fields=('username','userid',)
