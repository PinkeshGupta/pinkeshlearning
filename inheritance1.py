# class Myclass1:
#     pass
# class Myclass2:
#     pass
# class Myclass3:
#     pass

################################################
#   every class is child class of object        #
################################################


# print(issubclass(Myclass1,object))
# print(issubclass(Myclass2,object))
# print(issubclass(Myclass3,object))

#====================================================================================#
# The Process of acquiring properties parent class to child class is call inheritance
#====================================================================================#
# class Myparent:
#     def m1(self):
#         print("parent m1 method")

# class Child(Myparent):
#     def m2(self):
#         super().m1()
#         print("Child m2 method")

# c = Child()
# c.m2()


#  Variable Declaration in Parent and Child class
# class Parent:
#     a,b, =10,20

# class Child(Parent):
#     x,y =100,200
#     def add(self,i,j):
#         print(i+j)
#         print(self.a +self.b)
#         print(self.x+self.y)

# c = Child()
# c.add(1000,2000)

# Variables with same name
# class Parent:
#     a,b, =10,20

# class Child(Parent):
#     a,b =100,200
#     def add(self,a,b):
#         print(a+b)
#         print(self.a +self.b)
#         print(super().a+super().b)

# c = Child()
# c.add(1000,2000)


#Global variables

# a,b = 10000,20000
# class Parent:
#     a,b, =10,20

# class Child(Parent):
#     a,b =100,200
#     def add(self,a,b):
#         print(a+b)
#         print(self.a +self.b)
#         print(super().a+super().b)
#         print(globals()['a']+globals()['b'])

# c = Child()
# c.add(1000,2000)

# if constructor and methods are not available in child class then
# Parent class constructor or method is called 
# class Parent:
#     def __init__(self):
#         print("Parent class constructor")


# class Child(Parent):
#     pass

# c=Child()


# child class constructor is called below
# class Parent:
#     def __init__(self):
#         print("Parent class constructor")


# class Child(Parent):
#     def __init__(self):
        
#         print("Child class constructor")

# c=Child()



#calling super class constructor with child Type 1
# class Parent:
#     def __init__(self,name):
#         print("Parent class constructor",name)


# class Child(Parent):
#     def __init__(self):
#         super().__init__("Pinkesh")
#         print("Child class constructor")

# c=Child()



#calling super class constructor with child Type 2

# class Parent:
#     def __init__(self,name):
#         print("Parent class constructor",name)


# class Child(Parent):
#     def __init__(self):
#         super().__init__("Pinkesh")
#         Parent.__init__(self,"Gupta")
#         print("Child class constructor")

# c=Child()





    








