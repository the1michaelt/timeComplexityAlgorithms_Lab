# <!-- Task 4: Sort List
# Given a list of numbers, manually sort the list into ascending order (may not use built in .sort() method).
# Suggested strategy:
# Starting with the first two numbers, compare them to see which is larger. 
# Place the lower number to the left and the higher number to the right.
# Iterate through the list, checking each pair of numbers one at a time.
# Repeat from the start until the entire list is sorted.
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat. -->


# O notation 
def list_of_numbers_ascending():
    list_of_numbers= ["4","0","3","8","5","9"]
    index_number= 0
    index_number1 = 1
    end_index= int(len(list_of_numbers))
    
    while index_number1 < end_index: #should terminate at the number prior to the last in the string
        number1 = list_of_numbers[index_number]
        number2 = list_of_numbers[index_number1]
        if number1 > number2:
            # below should remove the greater number of the pair
            list_of_numbers.remove(list_of_numbers[index_number])
            # below should insert the removed number into the position behind the previous number
            list_of_numbers.insert(int(list_of_numbers[index_number1]), number1)
        #these control the pair
        index_number += 1 
        index_number1 += 1
           
list_of_numbers_ascending()


# def list_of_numbers_ascending():
#     list_of_numbers = ["4", "0", "3"]
#     index_number = 0
#     index_number1 = 1
#     end_index = int(len(list_of_numbers))

#     while index_number1 < end_index:
#         number1 = list_of_numbers[index_number]
#         number2 = list_of_numbers[index_number1]
#         if number1 > number2:
#             list_of_numbers.append(list_of_numbers[index_number])
#             list_of_numbers.remove(list_of_numbers[index_number])
#         index_number += 1
#         index_number1 += 1


# list_of_numbers_ascending()


# def list_of_numbers_ascending():
#     list_of_numbers= ["4","0","3"]
#     index_number= 0
#     index_number1 = 1
#     end_index= int(len(list_of_numbers))
    
#     while index_number < end_index:
#     # index1 == index2
#         if list_of_numbers[index_number] < list_of_numbers[index_number1]:
#             list_of_numbers.remove(list_of_numbers[index_number])
#             list_of_numbers.append(list_of_numbers[index_number])
#             index_number += 1 
#             index_number1 += 1
        
# list_of_numbers_ascending()

# Starting with the first two numbers, compare them to see which is larger. 

# Place the lower number to the left and the higher number to the right.
# Iterate through the list, checking each pair of numbers one at a time.
# Repeat from the start until the entire list is sorted.


# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat.

