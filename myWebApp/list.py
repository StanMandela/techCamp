""""
A list is a collection of more than one variable
They need not be of the same type
[]--declare a list

"""

x=["John Doe",20,"john@gmail.com","Nairobi", True]
print(x)
dishes=["Ugali","Samaki wa Kupakwa","Boilo","Nyama"]
colors=['Blue','white','grey']
combined=[dishes,colors,["Monday","Tuesday"]]

print(dishes)
print(colors)
print(combined)
#accessing items of nested lists
print(combined[2][1])
print("Length of list",len(combined))
print("Length of list",len(dishes))

#Concatination of lists
print("Concatinated lits",dishes + colors)
#del dishes[2]
print("sliced list",dishes[0:2])

 #POP()....removes the last element of the list
print("POP function on Colors list:-",colors.pop())

#Reverse() reverse the order of the elements
list1=[1,2,3,4,5]
list1.reverse()
print("Reverse function on colors list:-",list1)
colors.reverse()
print(colors)

#Append function- Adds elements ion a list
colors.append('brown')
print(colors)

#extend() adds the new elements into an existing
list2=["Jon","May","lil"]
another_list=[1,3,4,5,6]
list2.extend(another_list)
print(list2)

#Insert into a list
list2.insert(1,"kim")
print("Combined list", list2)

#COunt
u=list2.count("Jon")
print(u)
#len
print(len(list2))
