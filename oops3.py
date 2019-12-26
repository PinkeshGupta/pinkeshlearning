# how to modified static variables
# class Test:
#     a = int(input("Please enter first value \n"))

#     def __init__(self):
#         # self.a
#         Test.a = int(input("Please enter modified second value \n"))

#     @classmethod
#     def m1(cls):
#         cls.a = int(input("Please enter modified value inside classmethod \n"))
#     @staticmethod
#     def m2():
#         Test.a =int(input("Please enter modified value in staticmethod \n"))
#         print("New Values\n")

# t = Test()
# t.m1()
# Test.m2()
# t.a =50
# print(Test.a)
# print(t.a)


#================================================================================#
#                     How to delete static variable                              #
#================================================================================#
# 1. with in the class we use class name or cls if classmethod is there
# 2. out side the class only by using class name

# class Test:
#     a = int(input("Please enter first value \n"))

#     # def __init__(self):
#     #     del Test.a

#     def m1(self):
#         del Test.a
#         # self.a

#     # @classmethod
#     # def m1(cls):
#     #     cls.a = int(input("Please enter modified value inside classmethod \n"))
#     # @staticmethod
#     # def m2():
#     #     Test.a =int(input("Please enter modified value in staticmethod \n"))
#     #     print("New Values\n")

# print(Test.__dict__)
# t =Test()
# t.m1()
# print(Test.__dict__)




# x =1
# def f():
#     x =2
#     return x
# class C(object):
#     x=3
# if True:

#     x =4
# f()
# C()
# print(x)

# def f(a,*b,**c):
#     print("{}{}".format(len(b),len(c)))
# f(10,20,x=30)

# import re
# line = ('The quick, brown, fox')
# m = re.search("\w+(?=,)", line)
# # print(m)

# if m:
#     print(m.group('word'))

# The intention of this code is to find the first word in line that is 
# followed by a comma character i.e. ',' and print just the word (without the comma). 
# Thus, the above code should print quick (without the comma).

# What should replace the xxxxx for this code to work as described above?
#  (Your answer below should be a single expression that replaces xxxxx, and nothing else. 
#  And you are not allowed to change anything else in the give code.)


line = 'mary had a little tiger'
words = line.split()
# print(words)

len_sorted_words = sorted(words,key=lambda x: x.split()[1])
print(len_sorted_words)
print(' '.join(len_sorted_words))