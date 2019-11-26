""""


"""
pin = 1234
attmpt=3
x = 1

while x<=3:
    inp=int(input("Enter PIN"))
    if inp!=pin:
     attmpt=attmpt-1
     if attmpt ==0:
             print("Blocked")
     else:
         print("Wrong! You have {}".format(attmpt))
         x+=1
    else:
         print("Sucess")
         break





# z=list(range(1,21))
# print(z)

x= list(range(1,100))
evenno=[]
oddno=[]
print(x)
for i in x:
    if i %2 == 0 or i%3==0:
        evenno.append(i)
    else:
        oddno.append(i)
print(evenno)
print(oddno)



