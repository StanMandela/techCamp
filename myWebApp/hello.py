
print ("hello world")

#variable
name ="mandela"
print(name)
age = 30
gender="male"
married = True

# print(married)
# name="cecil"
# print(type(name))
#
# print(type(age))
# print(type(married))

status='Monday November 18'
#indexing
new_var=status[3]
#slicing - getting characters of a certain range

new_var=status[0:] #from the specified index to yhe end of the string
new_var2=status[9:13]
new_var3=status[9:17]
#
# print(new_var)
# print(new_var2)
# print(new_var3)

# length of the whole statement
print("The of Length of a string  is:")
string = "Python is awesome, isn't it?"
print("the number of characters is",len(  string))


#counting a Substring in a sentence

substring = "n"
count = string.count(substring)
print("The count of 'n' is :", count)
print(" For the exercise")

py= "We are learning how to program in python. I find python programming fun"
substring=" python"
count2= py.count(substring)
print("The count is:", count2)

print(" Write a Python function to reverses the word below: raven")
word="REVEN"
y= word[::-1] # [-1::-1] here we have three arguments # first is -1 that means start from last element
                                                        # second argument is empty that means move to end of list
                                                        # third arguments is difference of step
print(y)

#List-

