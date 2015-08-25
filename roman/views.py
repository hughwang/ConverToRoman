from django.shortcuts import render
from roman.forms import PostForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST) # Bind data from request.POST into a PostForm
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            original_number = form.cleaned_data['original_number']
            original_number = int(original_number)
            roman_number = convert_to_roman(original_number)
            context = {
                'original_number' : original_number,
                'result' : roman_number
            }
            return render(request, 'roman/result.html', context)
 
    return render(request, 'roman/index.html', {
        'form': form,
    })

def convert_to_roman (original_number):
    convert_table = (
        {'decimal': 1, 'roman': 'I'},
        {'decimal': 4, 'roman': 'IV'},
        {'decimal': 5, 'roman': 'V'},
        {'decimal': 9, 'roman': 'IX'},
        {'decimal': 10, 'roman': 'X'},
        {'decimal': 40, 'roman': 'XL'},
        {'decimal': 50, 'roman': 'L'},
        {'decimal': 90, 'roman': 'XC'},
        {'decimal': 100, 'roman': 'C'},
        {'decimal': 400, 'roman': 'CD'},
        {'decimal': 500, 'roman': 'D'},
        {'decimal': 900, 'roman': 'CM'},
        {'decimal': 1000, 'roman': 'M'},        
    )
    
    #1.From the above table, find the highest 'decimal' value v that is less than or equal to the 'decimal' number x 
    #  and its corresponding roman numeral n:
    
    #2.Write the roman numeral n that you found and subtract its value v from x:
    #  x = x - v

    #3.Repeat stages 1 and 2 until you get zero result of x.
    
    result_list=[]
    while(original_number > 0):
        for item in reversed(convert_table):
            if  item['decimal'] <= original_number:
                result_list.append(item['roman'])
                original_number = original_number - item['decimal']
                break
    else:
        return "".join(result_list)

 
