# Create a function that takes a list as a parameter,
# and returns a new list with all its element's values doubled.
# It should raise an error if the parameter is not a list.

test=[1,2,3]

def double(list):
    list_element_doubled=[]
    for i in range(len(list)):
        list_element_doubled.append(list[i] * 2)
    return list_element_doubled

print(double(test))
