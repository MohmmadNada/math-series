#1. in terminal:  poetry install
#1. in terminal:  poetry shell

# in casa we have - number or string  
def fibonacci(n):
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