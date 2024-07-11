def double(x):
    return x*2
print(double(5))

double =lambda x:x*2
print(double(5))
def apply(fx,value):
    return 6+fx(value)


cube= lambda i:i*i*i
# print(cube(5))


average= lambda  x,y:(x+y)/2
print(average(3,5))

print(apply(cube,2))

    