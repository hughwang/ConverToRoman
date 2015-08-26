import re

def convert_to_roman (original_number):
    # asume original_number is an integer
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
    
    # to convert x into roman numerial:
    # 1.From the above table, find the highest 'decimal' value v that is less than or equal to the 'decimal' number x 
    #  and its corresponding roman numeral n:
    
    # 2.Write the roman numeral n that you found and subtract its value v from x:
    #  x = x - v

    # 3.Repeat stages 1 and 2 until you get zero result of x.
    
    # use a list to store temporary calcualted roman numeral
    result_list=[]

    while(original_number > 0):
        # visit the convert_table in reversed order, to find highest 'decimal' first
        for item in reversed(convert_table):   
            if  item['decimal'] <= original_number:
                result_list.append(item['roman'])
                original_number = original_number - item['decimal']
                break
    else:
        return "".join(result_list)