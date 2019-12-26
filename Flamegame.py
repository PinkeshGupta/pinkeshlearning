first_name = input("Please enter fist name:").lower()
second_name = input("Please enter fist name:").lower()

first_name = first_name.replace(" ","")
second_name = second_name.replace(" ","")

print(first_name)
print(second_name)

for i in first_name:
    for j in second_name:
        if i == j:
            first_name =first_name.replace(i,"",1)
            second_name =second_name.replace(i,"",1)
            break
count = len(first_name+second_name)
print(count)

if count >0:
    list1 =["Friends","Lovers","Affectionate","Marriage","Enemies","Siblings"]
    while len(list1)>1:
        c = count%len(list1)-1
        if c >=0:
            left = list1[:c]
            right = list1[c+1:]
            list1 = right + left
        else:
            list1 = list1[:len(list1)-1]
    print("Relationship is: ",list1[0])
else:
    print("Enter different Names")
