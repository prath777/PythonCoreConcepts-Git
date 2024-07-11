# print("enter num1")
# num1=(input("Enter the first number"))
# print("enter num2")
# num2=(input("Enter the second number"))
# try:

#     print("Sum of two numbers is :",
#           int(num1)+int (num2))
# except Exception as e:
#     print(e)

# print("This line is very important")

# try:
#     open("this.txt")
# except Exception as e:
#     print(e)

# print("Program is running")

try:
    print("I will try this code and will throw exception if there is any problem")

except Exception as e:
    print(e)
else:
    print("This block is executed only if there is no exception")
finally:
    print("This will be printed in every case")