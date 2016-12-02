# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file does not exist, just return 0.

from collections import Counter

def num_of_letter(file_name):
    number_of_a = 0
    try:
        for i in file_name:
            if file_name[i] == 'a':
                number_of_a += 1
        return number_of_a
    except FileNotFoundError:
        return 0

print(num_of_letter(how_many_a.txt))
