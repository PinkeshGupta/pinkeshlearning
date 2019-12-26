# def duplicateval(my_lst):
#     freq = {}
#     for item in my_lst:
#         if (item in freq):
#             freq[item] += 1
#         else:
#             freq[item] = 1
#     for key, value in freq.items():
#         print("%d : %d" % (key, value))
#
#
# if __name__ == "__main__":
#     my_lst = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
#
#     duplicateval(my_lst)



def duplicateval(listval):
    frequency ={}
    for i in listval:
        if i in frequency:
            frequency[i]  +=1
        else:
            frequency[i] = 1

    for key,value in frequency.items():
        print("%d : %d" %(key,value))


if __name__ =="__main__":
    listval = [1, 3, 4, 4, 5, 2, 7, 7, 3, 1, 6, 8, 3, 2, 2, 1, 8, 6, 6]
    duplicateval(listval)

















