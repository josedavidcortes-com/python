"""
class david:
    course = 'DSA'

    def purchase(obj):
        print ("Purchase course: ", obj.course)

david.purchase = classmethod(david.purchase)
david.purchase()

"""

"""
class Student:
    
    #create a variable
    name = "Geeksforgeeks"

    #create a function
    def print_name(obj):
        print("The name is: ", obj.name)


Student.print_name = classmethod(Student.print_name)
Student.print_name()

"""


class Professor:
    
    name = 'PhD David Cortes'

    def get_fullname(obj):
        print ("Welcome to MIT Professor: ", Professor.name)
    
    skills = 'Quatum Physics'
    def get_skill(obj):
        print ("is an expert in: ", Professor.skills )

Professor.get_fullname = classmethod(Professor.get_fullname)
Professor.get_fullname()
Professor.get_skill = classmethod(Professor.get_skill)
Professor.get_skill()
