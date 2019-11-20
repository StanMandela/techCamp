"""

1.Logical Operators
//- Floor operator- division that results into a whole number
%- modlus
**- exponent
2.Comparision operators
>,<,==,!=,

"""
# x=34
# y=65
# print(x+y)
# print(x/y)
# print(x%y)
# print(x**y)
# print(y//x)
# print(y/x)


# x=int(input("Enter a number:"))
# y=int(input("Enter a number:"))
# z= x+y
# print(z)

# a=12
# b=13
# print("a > b", a>b)
# print("a < b", a<b)
# print("a == b", a==b)
# print("a != b", a!=b)

#LOGICAL OPERATORS
"""
    A       B         AND       OR      
    true    True    True        True
    True    False   false       true
    False    True   false       true
    False   False    False      False
"""
m= True
n=False
print("M and N", m and n)
print("M or N", m or n)
print(" not M is",  not m)

""" ASSIGNMENT OPERATIONS
    =
    += Add and assign
    -= Subtract and assign
"""
c= 190
print(c)
c+=40 #c=c+10
print(c)
c-=50 #c=c-50
print(c)
c*=4 #c= c*4
print(c)
 #Membership Operators
 #identity operators
 #bit operators

#Arithmetic
x= int(input("Enter a Number"))
y=int(input("Enter a Second Number"))
z=x+y
print("Sum is:",z)