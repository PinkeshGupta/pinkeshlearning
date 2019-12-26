# print("Twinkle, twinkle, little star, \n"\
#       "\t\tHow I wonder what you are! \n"\
#                         "\t\t\tUp above the world so high,\n"\
#                         "               Like a diamond in the sky.\n"\
#       "Twinkle, twinkle, little star,\n"\
#       "\t\tHow I wonder what you are")
# import  sys
#
# print(sys.version_info
#       )

# import datetime
# now =datetime.datetime.now()
# print("Current date and time is :")
# print (now.strftime("%Y-%m-%d %H:%M:%S"))

#
# from math import pi as p
#
# r= float(input("Please enter radius\n"))
# print("area of circle with radius "+str(r)+ "is " +str(p*r*r))
#
# f_name =input("Please enter our first name \n")
# f_last =input("Please enter our last name \n")
# print(f_last,f_name)
#

# values =input("Please enter values seperated b comma ',' \n")
#
# list =values.split(",")
# tuple = tuple(list)
# print("List: ",list)
# print("Tuple: ",tuple)
#
#
# filename =input("Please enter file name \n")
# extension =filename.split(".")
#
# print("File extension is",extension[-1])
#
#

# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],color_list[-1])
#

# exam_st_date = (11, 12, 2014)
# print("The examination date is %i / %i /%i" ,exam_st_date)
#
# n = int(input("enter a integer\n"))
# n1=int("%s"%n)
# n2=int("%s%s"%(n,n))
# n3=int("%s%s%s"%(n,n,n))
# print(n1+n2+n3)
    
# import calendar
#
#
# print(calendar.month(2019,11))
#



# num = int(input("Please enter number \n"))
# if num <= 17 :
#     result = 17 - num
#     print(result)
# elif num >17:
#     result1 = num -17
#     print(result1**2)
# else:
#     print("Invalid number")


# def summion(a,b,c):
#     sum = a + b + c

#     if(a==b==c):
#         sum = sum *3
#     return sum

# print(summion(5,10,15))
# print(summion(5,5,5))

# uname = input("Please enter you full name \n")

# print(f" upppercase name is {uname.upper()} and lowercase is {uname.lower()}")
# print(len(uname))


uinput,value =input("Please enter your name and one charater ").split(',')
print(f"charecter count from name is {uinput.strip().lower().count(value.strip().lower())}")



                              












