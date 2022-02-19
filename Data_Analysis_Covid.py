import csv
data_file = r"C:\Users\marci\OneDrive\Documentos\Proyectos Python\country_wise_latest.csv"
open_file = open (data_file)
print(open_file)
data_set = csv.reader(open_file)
print(data_set)


def average_cases():
    total = 0
    counter = 0
    for row in data_set:
        if(row[1] != "Confirmed"): 
            counter +=1
            total += int(row[1])
    return total/counter 
    

avg_cases = average_cases()
print(avg_cases)





