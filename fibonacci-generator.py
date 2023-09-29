#We simply ask the user to enter a number with the input
number = int(input("Please, enter the quantity of numbers to display (watchout, above 30/40 and depending on your computer, the output may take some minutes to display) : "))

#creating a recursive function 
def fibonacci_recursive(n):
    if n <= 1:
        #returning 1 allow us to be sure that the [0] and [1] elements of the list "range(number) are respectively equal to 0 and 1
        return n
    else:
        #when 0 and 1 are passed, we then start to make the sum of the 2 last numbers to create the last of the list
        return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)
    
#{0} represent a placeholder, and the .format() function represent the value of the placeholder
print("The firsts {0} numbers of the Fibonnaci sequence are : ".format(number), end = " ")

#we just make a loop with an iterator, asking for python to loop the functions until the iterator is equal to number
for i in range(number):
    print(fibonacci_recursive(i), end = " ")