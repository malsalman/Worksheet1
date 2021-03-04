#!/usr/bin/env python



import sys
sum_of_user_inputs=0
user_input=sys.argv
number_of_args = len(sys.argv)
if number_of_args>6:
    print("Error")
    
else: 
    for arg in user_input[1:]:
        try:
            val=int(arg)
            if True:
                sum_of_user_inputs+=int(arg)
        
        except ValueError:
            print("Please enter only integers")

print(sum_of_user_inputs)  