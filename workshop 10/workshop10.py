'''
Author: Akond Rahman 
Code needed for Workshop 10
'''

from ast import operator
import random 

def divide(v1, v2):
    temp = 0 
    if (isinstance(v1, int))  and (isinstance(v2, int)): 
       if v2 >  0:
          temp =  v1 / v2
       elif v2 < 0:
          temp = v1 / v2 
       else:
        
          temp = "Divisor is zero. Please Provide non-zero values."
    else: 
       temp = "Invalid input. Please provide numeric values."    
    return temp 

def fuzzValues():
    
    res = divide(2, 1)
    res = divide(2, 0)
    res = divide(2, -1)
    res = divide(2, '1')
    res = divide('2', '1')
    
    
  
    fuzzValues = [-1, -2, 1.00, 2.00, 0.00, 1/2, -1.00, -0, 'true', 'false', '¯\\_(ツ)_/¯', 'nil', 'undefined', 1, 2]
    

    for i in range(7):
      v1 = random.choice(fuzzValues)
      v2 = random.choice(fuzzValues)
      res = divide(v1, v2)
      print('v1 = {}, v2 = {}, res = {}'.format(v1, v2, res))
      print('='*100)

def simpleFuzzer(): 
    fuzzValues()


if __name__=='__main__':
    simpleFuzzer()
