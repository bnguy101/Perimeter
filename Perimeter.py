# defining the function
def calculate_rectangle_perimeter(length1,length2,length3,length4):
    perimeter = length1 + length2 + length3 + length4 
    return perimeter

# ask the user to input the value of each side
length1 = float(input("Enter the length of the rectangle side 1: "))
length2 = float(input("Enter the length of the rectangle side 2: "))
length3 = float(input("Enter the length of the rectangle side 3: "))
length4 = float(input("Enter the length of the rectangle side 4: "))

rectangle_perimeter = calculate_rectangle_perimeter(length1,length2,length3,length4)

# display the value the user inputs
print('This is your perimeter value', rectangle_perimeter)


