import numpy
import matplotlib.pyplot as plt 
import csv


data_file = r"C:\Users\marci\OneDrive\Documentos\Proyectos Python\country_wise_latest.csv"
open_file = open(data_file)
countries = []
deaths = []
data_set = csv.reader(open_file)

for row in data_set:
    countries.append(row[0])
    deaths.append(row[2])

countries.pop(0)
deaths.pop(0)
print(countries, deaths)
print(len(countries), len(deaths))

plt.title("Deaths by Country")
plt.plot(countries, deaths)
plt.show()

