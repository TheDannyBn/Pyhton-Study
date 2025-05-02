#Chapter 4 – Lists
#Create a list of 3 colors and print it.
#Add a new color to the list and print the updated list.
#Remove the second item from a list and print the result.
#Print the first item in a list using indexing.
#Use a for loop to print all items in a list.
#Check if a specific color is in the list.
#Sort a list of numbers in ascending order.
#Reverse a list and print it.
#Create an empty list and add 3 numbers using append().
#Count how many times a specific value appears in a list.


colors = ['red', 'blue', 'green']
print("colors:", colors)

colors.append("yellow")
print("New color added:", colors)

colors.pop(1)
print("After removing second color in list:", colors)

print("First color:", colors[0])

print("printing all colors with for loop:")
for color in colors:
    print(color)


check_color = "red"
print(f"Is {check_color} in list", check_color in colors)

numbers = [5,2,8,1,9]
numbers.sort()
print("Sorted numbers:" , numbers )

numbers.reverse()
print("Reversed numbers:", numbers)

empty_list=[]
empty_list.append(10)
empty_list.append(20)
empty_list.append(30)
print("Empty list with 3 numbers:", empty_list )

count_list = [1,2,2,3,2,4]
value = 2
print(f"Count of {value} in list:",count_list.count(value))