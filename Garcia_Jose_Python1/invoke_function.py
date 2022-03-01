import imp

from initialize_functions import *

'''
To use a function, you call it. When you call a function, you must provide values, or arguments, for each of the function’s parameters.
Functions allow you to write code efficiently. When you need to perform an action more than once, wrap that code in a function and call it when you need it. When you need to change how the action is carried out, you can change the code in the function, and the improvement is applied everywhere.
'''

print("Invoking zero arg function")
zero_arg_function()

print("Invoking function with required arguments")
introduction("Harry", "Houdini")

print("Invoking function with default arguments")
introduction_with_default_args()

#TODO: In this file, go ahead and invoke the rest of the functions from the initialize_functions.py file
print("Invoking zero arg function")
zero_arg_function()

print("Invoking Introduction Function")
introduction("Jose", "Garcia")

print("Invoking Introduction with default args function")
introduction_with_default_args()

print("Invoking Introduction with mix of default args")
introduction_with_mix_of_default_args("Jose")

print("Invoking product of two num function")
product_of_two_num(3,2)

print("Invoking add all nums function")
add_all_nums(5,6,7,8,10)

print("Invoking double function")
double(10)

print("Invoking fib function")
fib(10)

print("Invoking subtract funciton")
subtract(10,5)