
#Iterable-
#Iterator- 
#Iteration-

#Implementing iterator using  inbuilt functions  


# nums=[1,2,3,4,5]

# it=iter(nums)

# print(it.__next__())
# print(it.__next__())
# print(next(it))


#Implementing iterator using class function..

#If we don't want to use inbuilt function.
# then you can built your own object for iterator using class

#Two important methods we need in Iteration

# iter()-It will give you the object of the iterator
#next()-It will give you the next value or next object



class TopTen:
     def __init__(self):
          self.num=1
    
    
     def __iter__(self):
          return self

     def __next__(self):
          if(self.num<=10):
            val=self.num
            self.num+=1
            return val
          else:
              raise StopIteration
              
values=TopTen()
print(next(values))# Here 1 is print then 1 is not print again in loop.

for i in values:
    print(i)

  