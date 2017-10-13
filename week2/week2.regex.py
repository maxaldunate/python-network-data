# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:43:38 2017

@author: Max
"""
import re
sample_file = open('assigment_regex_sum_40675.txt','r')
sample_file = sample_file.read()
numbers = re.findall('[0-9]+',sample_file)
numbers = list(map(int, numbers))
result = sum(numbers)
print(result)
print('')
print('')


# UGLY but shorter version
print(sum(list(map(int, re.findall('[0-9]+',open('assigment_regex_sum_40675.txt','r').read())))))

