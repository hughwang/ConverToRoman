from django import forms
 
class PostForm(forms.Form):
    original_number = forms.CharField(max_length=4)

