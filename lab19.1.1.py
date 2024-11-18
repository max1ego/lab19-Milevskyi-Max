import pickle
import random
import string

n = int(input("Введіть довжину списку: "))

random_list = []
for i in range(n):
    if i % 2 == 0:  
        random_list.append(str(random.randint(0, 9)))  
    else:  
        random_list.append(random.choice(string.ascii_letters))  

with open("random_list.pkl", "wb") as file:
    pickle.dump(random_list, file)

print("Список успішно записаний у файл.")
