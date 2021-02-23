# grades.py
# A program that stores a student name and a list of her courses and grades in a dict, the program should then print out her data.
# Author: Andy Walker

student = {
    "Name": "Mary",
    "modules": [
        {
            "courseName": "Programming",
            "Grade": "45",
            "Semester": "Spring"
        },
        {    
            "courseName": "History",
            "Grade": "99",
            "Semester": "Winter"
        }
    ]
}

print ("Student: {}".format(student["Name"]))

for module in student["modules"]:
    print ("\t {} \t: {} \t: {}".format(module["courseName"], module["Grade"], module["Semester"]))