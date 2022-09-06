# <!-- Task 2: Less than 100
# Given a list of numbers, determine if each item in the list is lower than 100.
# The function should take in the list as a parameter and return a boolean value (False if there are any numbers greater than 100, True if all numbers are less than 100).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat. -->


#O notation O(1)-- One input. the boolean value will be determined solely by the end number's relationship to the number 100. 

def list_of_numbers(): 
    start_number= int(input('\nGiven a range of numbers, this algorithm will determine if all numbers are less than 100.\n\nTo begin, please enter any number greater than 0 to start this range. '))
    end_number= int(input('Please enter any number to end that range. '))
    if end_number > 100:
        return False
    return True
list_of_numbers()


