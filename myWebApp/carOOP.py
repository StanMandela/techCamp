class Car:
    wheel_type ="Firestone"
    make="Mercedes"
    year_of_manufacture=2016
    #Runs as soon as you create an Object
    def __init__(self,milage,age):
        print(" I am the constructore method")
        self.milage=milage
        self.miaka=age


    def stopDist(self):
        print("{} stopping distance is 30M".format(self.name))

    def park(self):
        print("{} is currently parking".format(self.name))

# car1= Car()
#car1.name="X6"
# car1.stopDist()
# car2=Car()
# car2.name="Telsa CyberTruck"
# car2.park()

car3=Car(123,6)
car3.name="Jane"
print(car3.milage)
print(car3.miaka)
print(car3.name)


"""
Student Class
con method:

method :
1.to find total marks- totalMarks()
2.Find the avg core- averageScore()
3.grade the student-gradeStudent()

"""


