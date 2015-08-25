from django import forms
from django.core.exceptions import ValidationError
import re

def validate_1_to_3999(value):
    if re.match('^\d{1,4}$', value):
        value=int(value)
        if value < 1 or value > 3999:
            raise ValidationError('%s is not an integer between 1 to 3999' % value)
    else:
        raise ValidationError('%s is not an integer between 1 to 3999' % value)



class PostForm(forms.Form):
    original_number = forms.CharField( 
        validators=[validate_1_to_3999], 
        label='base-10 integer',
        max_length=4, 
	min_length=1,
	help_text='Please input an integer between 1 and 3999',
	widget=forms.TextInput(attrs={'class':'original_integer'}), 
    )



