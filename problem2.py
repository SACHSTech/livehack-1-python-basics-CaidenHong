'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose: Divides chicken with students and gives the remainder of the chicken to the teacher.bin	

Author:	Hong.C

Created:	date in 07/12/2020
------------------------------------------------------------------------------
'''
# Title
print("\n***** Welcome to the Chicken Distrubutor *****")

# Input for the amount of chicken and amount of people
students = input("\nHow Many Students In The Class: ")
chicken = input("How Pieces of Chicken: ")

# Calculations
chicken_for_students = float(chicken) / float(students)
chicken_for_fabroa = float(chicken) % float(students)

#Output
print("\nEach Student Will get " + str(int(chicken_for_students)) + " Pieces of Chicken and Mr. Fabroa will get " + str(int(chicken_for_fabroa)) + " Pieces of Chicken")


'''
need input of chicken
need input of students

chicken / students
remeber to int the final product

chicken % students
int product final 
'''