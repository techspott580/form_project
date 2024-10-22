from django import forms

class studentform(forms.Form):
    name=forms.CharField(max_length=30)
    rollno=forms.IntegerField()
    marks=forms.IntegerField()