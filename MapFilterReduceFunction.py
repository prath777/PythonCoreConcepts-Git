
# def cube(x):
#     return x*x*x
# l=[1,2,3,4,5]
# # newl=list(map(cube,l))

# newl=list(map(lambda x:x*x*x,l))#implenting lambda function with map

# print(newl) 

# # Filter
# def filter_function(a):
#     return a>2

# newnewl=list(filter(filter_function,l))
# print(newnewl)

from  functools import reduce

numbers=[1,2,3,4,5]

sum=reduce(lambda x,y:x+y,numbers)
print(sum)



