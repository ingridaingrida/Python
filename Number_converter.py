# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 22:43:14 2019

@author: ingrida grigonyte
"""

def converter(text):
    message_1 = 'Invalid input!'
    message_2 = 'Please enter a number!'
    message_3 = 'Please enter arabic or roman numbers only!'
    message_4 = 'Number is too big for the arabic to roman number conversion!'
    message_5 = 'Romans had no zero! No wonder they collapsed.'
    message_6 = 'Invalid combination of roman numerals.'
    
    if text == '' :
        print(message_2)
        return message_2

    if check_input(text) is True:
        kind = check_kind(text)
        if kind == 'arabic':
            if int(text) > 3999:
                print(message_4)
            elif int(text) == 0:
                print(message_5)
            else:
                converted_text = arabic_to_roman(text)
                print('Roman number is: ' + converted_text)
        elif kind == 'roman':
            converted_text = roman_to_arabic(text)
            if converted_text == 'Invalid combination':
                print(message_6)
            else:
                print('Arabic number is: ' +  converted_text)
        else:
            print(message_3)
    else:
        print(message_1)
        
        
def check_input(text):
   
    allowed = ['0','1','2','3','4','5','6','7','8','9','I','V','X','L','C','D','M']
    text_list = list(text)
    
    for i in text_list:
        if i not in allowed:
            return False 
    return True
    

def check_kind(text_to_check):
    arabic = ['0','1','2','3','4','5','6','7','8','9']
    roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    
    if text_to_check[0] in arabic:
        for i in text_to_check:
            if i not in arabic:
                return False
            else:            
                kind = 'arabic'
    elif text_to_check[0] in roman:
        for i in text_to_check:
            if i not in roman:
                return False
            else:
                kind = 'roman'
    return kind


def arabic_to_roman(text_to_convert):
    roman_list = []
    
    rom_numb = {
        0 : '',
        1 : 'I',          
        2 : 'II',
        3 : 'III',
        4 : 'IV',
        5 : 'V',
        6 : 'VI',
        7 : 'VII',
        8 : 'VIII',
        9 : 'IX',
        10 : 'X',
        20 : 'XX',
        30 : 'XXX',
        40 : 'XL',
        50 : 'L',
        60 : 'LX',
        70 : 'LXX', 
        80 : 'LXXX',
        90 : 'XC',
        100 : 'C',
        200 : 'CC',
        300 : 'CCC',
        400 : 'CD',
        500 : 'D',
        600 : 'DC',
        700 : 'DCC',
        800 : 'DCCC',
        900 : 'CM',
        1000 : 'M',
        2000 : 'MM',
        3000 : 'MMM'
    }
    
    text_list = list(text_to_convert)
    digit_list = [int(i) for i in text_list]
    for i in range(len(digit_list)):
        digit_list[i] *= 10**(len(digit_list) - i - 1)  
        roman_list.append(rom_numb[digit_list[i]])
        
    converted_to_ro = ''.join(roman_list)
    
    return(converted_to_ro)
         
   
def roman_to_arabic(text_to_convert): #TODO: EXCEPTIONS if invalid combinations
    message = 'Invalid combination'
    arabic_num = 0
    flag = 0
    i = 0
    sequential_m = 0
    sequential_d = 0
    sequential_c = 0
    sequential_l = 0
    sequential_x = 0
    sequential_v = 0
    sequential_i = 0
    flag_cmd = 0
    flag_xcl = 0
    flag_ixv = 0
    roman_num_list = list(text_to_convert)
    
    while (i < len(roman_num_list)):
        if roman_num_list[i] == 'M':
            if arabic_num % 1000 != 0:
                return message
            arabic_num += 1000
            sequential_m += 1
            if sequential_m > 3:
                return message               
            
        if roman_num_list[i] == 'D':
            if arabic_num % 500 != 0:
                return message
            arabic_num += 500
            sequential_d += 1
            if sequential_d > 1:
                return message               
            
        if roman_num_list[i] == 'C':
            if arabic_num % 100 != 0:
                return message
            if i != len(roman_num_list) - 1:  
                if roman_num_list[i + 1] == 'M':
                    if arabic_num % 1000 != 0:
                        return message
                    arabic_num += 900
                    flag = 1
                    flag_cmd +=1
                    if flag_cmd > 1:
                        return message
                elif roman_num_list[i + 1] == 'D':
                    if arabic_num % 1000 != 0:
                        return message
                    arabic_num += 400
                    flag = 1
                    flag_cmd += 1
                    if flag_cmd > 1:
                        return message
                else:
                    arabic_num += 100
                    sequential_c += 1
                    if (sequential_c > 3 or flag_cmd > 0):
                        return message               
            else:
                arabic_num += 100
                sequential_c += 1
                if (sequential_c > 3 or flag_cmd > 0):
                    return message               
        
        if roman_num_list[i] == 'L':
            if arabic_num % 50 != 0:
                return message
            arabic_num += 50
            sequential_l += 1
            if sequential_l > 1:
                return message               
            
        if roman_num_list[i] == 'X':
            if arabic_num % 10 != 0:
                return message
            if i != len(roman_num_list) - 1:         
                if roman_num_list[i + 1] == 'C':
                    if arabic_num % 100 != 0:
                        return message
                    arabic_num += 90
                    flag = 1
                    flag_xcl += 1
                    if flag_xcl > 1:
                        return message
                elif roman_num_list[i + 1] == 'L':
                    if arabic_num % 100 != 0:
                        return message
                    arabic_num += 40
                    flag = 1
                    flag_xcl += 1
                    if flag_xcl > 1:
                        return message
                else:
                    arabic_num += 10 
                    sequential_x += 1
                    if (sequential_x > 3 or flag_xcl > 0):
                        return message               
            else:
                arabic_num += 10
                sequential_x += 1
                if (sequential_x > 3 or flag_xcl > 0):
                    return message               
                
        if roman_num_list[i] == 'V':
            if arabic_num % 5 != 0:
                return message
            arabic_num += 5
            sequential_v += 1
            if sequential_v > 1:
                return message               
            
        if roman_num_list[i] == 'I':
            if i != len(roman_num_list) - 1:
                if roman_num_list[i + 1] == 'X':
                    if arabic_num % 10 != 0:
                        return message
                    arabic_num += 9
                    flag = 1
                    flag_ixv += 1
                    if flag_ixv > 1:
                        return message
                elif roman_num_list[i + 1] == 'V':
                    if arabic_num % 10 != 0:
                        return message
                    arabic_num += 4
                    flag = 1
                    flag_ixv += 1
                    if flag_ixv > 1:
                        return message
                else:
                    arabic_num += 1
                    sequential_i += 1
                    if (sequential_i > 3 or flag_ixv > 0):
                        return message               
            else:
                arabic_num += 1
                sequential_i += 1
                if (sequential_i > 3 or flag_ixv > 0):
                    return message               
        if flag > 0:
            i += 2               
            flag = 0
        else:
            i += 1
    
    return str(arabic_num)
#---------------------------------------------------------------------------#
number = input("Enter a number: ") 

text = str(number).upper().strip().replace(' ', '')

converter(text);


