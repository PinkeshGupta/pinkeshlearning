# difference between list and tuples
# Major difference between list and tuple is list is mutable whereas tuple is not
# ex 
# my_list=[1,2,3]
# print(my_list)
# my_list[2]= 5
# print(my_list)

# mu_tuple =(1,2,3)
# print(mu_tuple)

# mu_tuple[1]=2
# print(mu_tuple)

# import copy
# help(copy.copy)
# import os
# print(os.getcwd())

# my_list=[1,2,3]
# my_list.insert(3,4)
# print(my_list)
# my_list.reverse()

# print(my_list)

# my_list[::-1]

# print(my_list)

# import numpy

# x = numpy.array([[1, 2], [4, 5]]) 
# y = numpy.array([[7, 8], [9, 10]])


# print(numpy.dot(x,y))








# Python program to count perfect squares between a and b 



def PSNBV(firstnum,lastnum):
    count = 0
    
    for i in range(firstnum,lastnum+1):

        j =1
        while j*j <= i:

            if j*j ==i:
                count =count + 1
        
            j =j+1
        i =i+1
    return(count)



print(PSNBV(9,16))
        

# find GCD of give number

# def findGCD(a,b):
#     if a > b:
#         small =b
#     else:
#         small = a
#     for i in range(1,small+1):
            
#         if ((a % i == 0)) and ((b%i == 0)):
#             gcd = i
#     return gcd

# print(findGCD(60,48))

# def findGCD(a,b):
#     while(b):
#         a,b = b,a%b
#     return a

# print(findGCD(60,48))






























