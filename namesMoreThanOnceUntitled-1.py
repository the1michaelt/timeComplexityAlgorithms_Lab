# <!-- Task 3: Repeated Names
# Given a list of names, determine if any names are contained in the list more than once.
# The function should take in the list as a parameter and return a boolean value (True if there are any repeated names, False if there are no repeats).
# Leave a comment above the function stating the time complexity.
# Send a screenshot of your solution and time complexity comment to your personal instructors chat. -->

#O notation-- O(n!) factorial. calculate each  
name = ["smith", "joe", "smith"]

def names_listed_more_than_once(name):
    if name[0] == name[1] or name[0] == name[2]:
        return True
    elif name[1] == name[2]:
        return True
    else:
        return False

names_listed_more_than_once(name)
