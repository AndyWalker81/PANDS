# students.py
# Author: Andy Walker
students = []
filename = "students.json"
import json


def writeDict(obj):
    with open(filename, "wt") as f:
        json.dump(obj,f)

def readDict():
    with open(filename) as f:
        return json.load(f)    

def displayMenu():
    print ("What would you like to do?")
    print ("\t(a) Add new student")
    print ("\t(v) View students")
    print ("\t(s) Save students")
    print ("\t(l) Load students")
    print ("\t(q) Quit")
    choice = input ("Type one letter (a/v/s/l/q):").strip()
    return choice

def doAdd():
    currentStudent = {}
    currentStudent["name"] = input("Enter name: ")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\tEnter the module name (blank to quit): ").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)
        moduleName = input("\tEnter the next module name (blank to quit): ").strip()
    return modules

def displayModules():
    print ("\tName \tGrade")
    for module in modules:
        print ("\t{} \t{}".format(module["name"], module["grade"]))   

def doView():
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"]);

def doSave():
    writeDict(students)
    print ("students saved") 
    
def doLoad():
    global students
    students = readDict()
    print ("students loaded")
    
#main function
choice = displayMenu()
while(choice != 'q'):
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice == "s":
        doSave()
    elif choice == "l":
        doLoad()
    elif choice != 'q':
        print("\nplease select eiher a, v, s, l, or q\n")
    choice = displayMenu()