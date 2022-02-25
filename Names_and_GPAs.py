import numpy
import matplotlib.pyplot as mpl 
import random

Names = ["Ahmed", "Tory", "David", "Lucy", "Monica", "Diego", "Sebastian", "Juan", "Mary", "Kim"]
GPA = []

def gpa_generator(names):
    gpa_list = []
    for student in names:
        gpa_list.append(random.randint(0,100))
    return gpa_list

GPA = gpa_generator(Names)



mpl.title("Python Course: Students' GPA",fontweight="bold", color = "mediumvioletred", fontsize="10", horizontalalignment="center" )
colors = []
for value in GPA:
    if value < 50:
        colors.append("darkviolet")
    elif value < 60:
        colors.append("mediumorchid")
    else: 
        colors.append("violet")

mpl.bar(x = Names, height = GPA, width =0.9, color = colors)
mpl.grid(True)
mpl.xlabel("Student Names", fontweight="bold", color = "deeppink", fontsize="10", horizontalalignment="center")
mpl.ylabel("GPA",fontweight="bold", color = "deeppink", fontsize="10", horizontalalignment="center" )
mpl.show()