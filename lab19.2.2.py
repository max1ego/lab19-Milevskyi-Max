import shelve

with shelve.open("athletes_data") as db:
    athletes = db["athletes"]

sorted_athletes = sorted(athletes.items(), key=lambda x: x[1])

print("Переможці:")
for i, (name, time) in enumerate(sorted_athletes[:3], start=1):
    print(f"{i} місце: {name}, час: {time:.2f} хв")
