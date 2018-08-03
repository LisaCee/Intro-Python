# Write a function is_even that will return true if the passed in number is even.
def is_even(n):
    return n % 2 == 0

# print(is_even(5))    
# Read a number from the keyboard
num = input("Enter a number: ")
if int(num) % 2 == 0:
    print('Even!')
else: 
    print('Odd')    
# Print out "Even!" if the number is even. Otherwise print "Odd"