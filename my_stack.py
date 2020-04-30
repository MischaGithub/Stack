#Program to demonstrate stack implementation
#Craeting two list
my_stack = []
my_history = ["google.co.za", "money.co.za", "cars.com", "fb.com"]

#Craeting the function to add to the list
def add_to_stack(my_history):
    """
    >>> add_to_stack(['google.co.za', 'money.co.za', 'cars.com', 'fb.com'])
    ['google.co.za', 'money.co.za', 'cars.com', 'fb.com']
    """
    for h in my_history:
        my_stack.append(h)
    return my_stack

#Creating the function to remove an element from the list
def remove_from_stack(my_stack):
    """
    >>> remove_from_stack(['google.co.za', 'money.co.za', 'cars.com', 'fb.com'])
    ['google.co.za', 'money.co.za', 'cars.com']
    """
    my_stack.pop()
    return my_stack

print(add_to_stack(my_history))
print(remove_from_stack(my_stack))