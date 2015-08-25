from django.shortcuts import render
from roman.forms import PostForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from dbgp.client import brk

def index(request):
    #brk(host='127.0.0.1', port=53891)
    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST) # Bind data from request.POST into a PostForm
 
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            original_number = form.cleaned_data['original_number']
            roman_number = convert_to_roman(original_number)
            context = {'result' : roman_number}
            return render(request, 'roman/result.html', context)

 
    return render(request, 'roman/index.html', {
        'form': form,
    })

def convert_to_roman (original_number):
    return "Converted %s to roman number %s" % (original_number,original_number )

 
