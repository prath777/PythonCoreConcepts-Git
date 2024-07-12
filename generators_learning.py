# Type 1 By making objects

# def my_generator():
#     for i in range(10):
#         yield i
# gen=my_generator()

# for j in gen:
#     print(j)

#Type 2 by defining in yield

def my_genratorfun():
    yield 1
    yield 2
    yield 3

for value in my_genratorfun():
    print(value)