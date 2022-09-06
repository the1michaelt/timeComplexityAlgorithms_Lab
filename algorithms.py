import math
#task 1
# Given a numeric value, determine if it is even or odd.
# The function should take the value in as a parameter and return a boolean value(True if even, False if odd).

# O notation -- O(1). "Constant" as this calculation will always require just one iteration per input.
def even_or_odd():
    numeric_value = int(input('Please enter a number to determine if it is even. The result will be True or False. '))
    numeric_value %= 2
    if numeric_value==0:
        return True
    else:
        return False
even_or_odd()    

