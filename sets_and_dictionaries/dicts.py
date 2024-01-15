a = dict( name = "Brian Kimathi", age = 23, country = "Kenya")


# print(a.keys())
# print(a.values())

# print(a.items())

for key, value in a.items():
    print(f"{key}: {value}")

a["Is_married"] = False

print(a)

a.pop("name")

print(a)

a.popitem()
print(a)
a.update({"name": "Brian"})

print(a)