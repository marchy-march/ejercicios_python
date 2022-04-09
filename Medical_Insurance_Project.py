
import csv 
import pandas as pd
import numpy as np 

data_file = r"C:\Users\marci\OneDrive\Documentos\Proyectos Python\insurance.csv"
open_file = open(data_file)
data_set = csv.reader(open_file)
# print(data_set) why is it not printing? is there a way to show only a header? 

region_array = data_set["region"].unique()
#TypeError: '_csv.reader' object is not subscriptable
region_list = region_array.tolist()
