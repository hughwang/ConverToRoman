from django import forms
import re

class PostForm(forms.Form):
    original_number = forms.CharField( 
        label='base-10 integer',
        max_length=4, 
	min_length=1,
	help_text='Please input an integer between 1 and 3999',
	widget=forms.TextInput(attrs={'class':'original_integer'}), 
    )

    def clean_original_number(self):
        original_number = self.cleaned_data['original_number']
	if re.match('^\d{1,4}$', original_number):
            value=int(original_number)
            if value < 1 or value > 3999:
                raise forms.ValidationError('%s is not an integer between 1 to 3999' % value)
            else:
	        return value
        else:
            raise forms.ValidationError('%s is not an integer between 1 to 3999' % original_number)

    	



