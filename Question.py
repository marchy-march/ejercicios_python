class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker

  def estimated_insurance_cost(self):
    estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    print(str(self.name)+"’s estimated insurance costs is "+str(estimated_cost)+"dollars.")
    
  def estimated_insurance_cost2(self, name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * self - 12500
    print(str(name)+"’s estimated insurance costs is "+str(estimated_cost)+"dollars.")

    # add more parameters here
patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.name)
print(patient1.estimated_insurance_cost())
#patient1.estimated_insurance_cost2()


#why are we using class variables? what is the difference between estimated_insurance and estimated_insurance2? what does it mean to define a method within a class?



access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']
import csv
with open("logger.csv", "w") as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames = fields)
  log_writer.writeheader()
  for item in access_log:
    log_writer.writerow(item)
  print(logger_csv)



  #how can i print the new csv file?? iterando con .read y luego .readlines 


  with open("cool_dogs.txt", "a") as cool_dogs_file:
    cool_dogs_file.write("Air Buddy")
    print(cool_dogs_file)


  #when printing i get: <_io.TextIOWrapper name='cool_dogs.txt' mode='a' encoding='UTF-8'> same as above