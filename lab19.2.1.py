import shelve

athletes = {
    "Іваненко": 10.5,
    "Петренко": 9.8,
    "Сидоренко": 11.0,
    "Коваленко": 9.6,
    "Шевченко": 10.2
}

with shelve.open("athletes_data") as db:
    db["athletes"] = athletes

print("Дані про спортсменів збережено у файл.")
