#!/usr/bin/env python3

import sys 
import statistics 



def main(args):
    operations=[]
    numbers=[]

    for user_input in args[1:]:
        if user_input== '--mean' or user_input=='--mode' or user_input=='--median':
            operations.append(user_input)
         
        else:
            try:
                int(user_input)
                if True:
                    numbers.append(int(user_input))
            except ValueError:
                continue
            
     
            
    if len(operations)==0 and len(numbers)==0:
       print("Error") 
       
    elif len(operations)==0:
             mean=statistics.mean(numbers)
             print("The mean is: ", mean)
             
             mode=statistics.mode(numbers)
             print("The mode is: ", mode)
             
             median=statistics.median(numbers)
             print("The median is: ", median)
             
    else:
        for math_op in operations:
             if math_op == '--mean':
                 mean=statistics.mean(numbers)
                 print("The mean is: ", mean)
                 
             elif math_op  == '--mode':
                 mode=statistics.mode(numbers)
                 print("The mode is: ", mode)
                 
             elif math_op  == '--median':
                 median=statistics.median(numbers)
                 print("The median is: ", median)
    
    
if __name__=='__main__':
    main(sys.argv)
