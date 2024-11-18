import pickle

with open("random_list.pkl", "rb") as file:
    loaded_list = pickle.load(file)

print("Список зчитано з файлу:")
print(loaded_list)
