#OOP paradigm

class Person:
    #Class attribute//Properties
    species="Homo sapien sapien"

    #Methods- functions defined inside a class
    #def key word
    def walk(self):
        print("{} Is walking".format(self.name))
    def sleep(self):
        print("{} Is sleeping".format(self.name)) #.format to access the  instance attribute to be input with the object

p1= Person()
p2=Person()
print(p1.species)
p1.name="Stan"
p2.name="shishi"

p1.age=45
p1.job="Manager"
p1.style="Casual-smart"
p1.car="BMW"
print(p1.name)
p1.walk()
p2.sleep()


# p2.name="Mandela"
# p2.age=34
