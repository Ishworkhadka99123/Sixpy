'''
#6. Solve each of the following problem using Python Script.
# Make sure you use appropriate variable names ans comments.
#When there is a final answer have Python print it ti thr screen.
#A person's body mass index (BMI) is defined as : BMI=mass in kg/(height in m)2
'''

mass = float (input("Enter the mass of person in kg:"))
height=float(input("Enter the height of a person in meter :"))
BMI=(mass/(height*height))
print(f"The BMI index of a person is {BMI}")