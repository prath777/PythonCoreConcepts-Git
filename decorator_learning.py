def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx

# Modifying the function using decorators
@greet
def hello():
    print("Hello world")

hello()







# def greet(fx):
#     def mfx(a, b):
#         a, b = int(a), int(b)
#         result = fx(a, b)  # Call the original function and store the result
#         print("Thanks for using this function")
#         return result  # Return the result
#     return mfx

# Modifying the function using decorators
# @greet
# def mysum(a, b):
#     return a + b

# print(mysum("2", "5"))  # This should work correctly now

#For Understanding

# my_sum = greet(mysum(a,b))