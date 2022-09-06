# <!-- Task 2: Less than 100
# Given a list of numbers, determine if each item in the list is lower than 100.
# The function should take in the list as a parameter and return a boolean value (False if there are any numbers greater than 100, True if all numbers are less than 100).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat. -->


#O notation O(n)-- the number of loops will vary by the range of user-defined numbers. 

def list_of_numbers(): 
    start_number= int(input('\nGiven a range of numbers, this algorithm will determine how many of those numbers are less than 100.\n\nTo begin, please enter any number greater than 0 to start this range. '))
    end_number= int(input('Please enter any number to end that range. '))
    count = 0
    while count <= end_number:
        if start_number < 100:
            start_number += 1
            count +=1
        else:
            print(count, ' of these numbers are less than 100.')
            break
list_of_numbers()


