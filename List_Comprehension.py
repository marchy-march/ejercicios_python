import random

list1 = []
for x in range(1,1001):
    if x%7==0:
        list1.append(x)

list2 = [x for x in range(1,1001) if x%7 ==0]
print(list2)


Lst1 = []
for x in range(1,1001): 
    if "3" in str(x): 
        Lst1.append(x)

Lst1 = [x for x in range(1,1001) if "3" in str(x)]
print(Lst1)


list5 = ["cat", "dog", "iguana", "tiger", "elephant"]
no_vowels = []
vowels = ["a", "e", "i", "o", "u"]
# for i in range(len(list5)):
#     for x in vowels:
#         if x not in list5[i]:
#             continue
#         else:
#             no_vowels.append(list5[i].replace(x,""))


for i in list5:
    no_vowels.append("".join([l for l in i if l not in vowels]))

            

print(no_vowels)





list7 = []
lst8 = [random.randint(1,100) for x in range(101)] 
lst9 = [random.randint(1,100) for x in range(101)] 
for i in lst8:
    if i in lst9:
        list7.append(i)

print(sorted(lst8))
print(sort(lst9))

list10 = [i for i in lst8 if i in lst9]
print(sorted(list10))