#1. in terminal:  poetry install
#1. in terminal:  poetry shell
'''
> but the lab asks you to ensure that your function(s) has a well-formed docstring
> finally Submit a Link to README.md

'''
# in casa we have - number or string  
def fibonacci(n):
    '''
    The Fibonacci Series is a numeric series starting with the integers 0 and 1. In this series, the next integer is determined by summing the previous two. This gives us:
    function should return the nth(from argument) value in the fibonacci series. 
    '''
    if type(n)==type("0") or n<0:
        return "input must be number"
    else:  
        list_fibonacci=[0,1]
        j =0
        while j < n:
            j+=1
            sum=list_fibonacci[-1]+list_fibonacci[-2]
            list_fibonacci.append(sum)
        return list_fibonacci[n]

def lucas(n):
    '''
    The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. 
    returns the nth value in the lucas numbers Again
    '''
    if type(n)==type("0") or n<0:
        return "input must be number"
    else:    
        list_lucas =[2,1]
        j =0
        while j < n:
            j+=1
            sum=list_lucas[-1]+list_lucas[-2]
            list_lucas.append(sum)
        return list_lucas[n]
# The required parameter will determine which element in the series to print.
# The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced.
def sum_series(n, item_one=0, item_tow=1):
    '''
    function return nth value from array related series of integers , start with two base value then sum value from two previous values
    the funtion takes one required parameter and two optional parameters. 
    The required parameter will determine which element in the series to print. The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced. 
    Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will produce other series. Again, you may use recursion or iteration, or both. Again, ensure that your function has a well-formed docstring.
    '''
    if type(n)==type("0") or n<0:
        return "input must be number"
    else:    
        if (item_one == 0 and item_tow == 1):
            return fibonacci(n)
        elif (item_one == 2 and item_tow == 1):
            return lucas(n)
        else:
            print('from else ')
            list_with_optional_input = [item_one, item_tow]
            j = 0
            while j < n:
                j += 1
                sum = list_with_optional_input[-1] + list_with_optional_input[-2]
                list_with_optional_input.append(sum)
            return list_with_optional_input[n]