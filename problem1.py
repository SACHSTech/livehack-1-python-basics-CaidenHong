'''
-------------------------------------------------------------------------------
Name:		problem1.py
Purpose:	Convert C to F

Author:	Hong.C

Created:	date in 07/12/2020
------------------------------------------------------------------------------
'''

# Title
print("***** Welcome to the Celsius to Fahrenheit Converter *****")

# User input
temp_c = float(input("\nWhat is the Temperature in Celsius: "))

# Calculation
temp_f = temp_c * 1.8 + 32
temp_f_rounded = round (temp_f,1)

# Output
print("\nYour Temperature in Fahrenheit is: " + str(temp_f_rounded) + " F")