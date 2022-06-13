from dataclasses import field
from tkinter import Widget
from django import forms
from .models import *

class MainpostForm(forms.ModelForm):
    class Meta:
        model=Mainpost
        fields=['title','text']
      
        labels={
            'title':'제목',
            'text':'내용',
        }