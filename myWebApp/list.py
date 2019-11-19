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






