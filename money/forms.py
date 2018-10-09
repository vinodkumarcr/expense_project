from django import forms
from .models import Expense,Share

class FormView(forms.ModelForm):
        class Meta():
            model= Expense
            fields=["Catagory","Date","Money","Place"]



class ShareView(forms.ModelForm):
    class Meta():
        model=Share
        fields='__all__'
