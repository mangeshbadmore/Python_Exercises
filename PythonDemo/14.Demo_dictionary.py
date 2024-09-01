# Traditional way of defining dictionary
# d1 = {

#     "name": "Mangesh",
#     "country": "India"
# }

# print(d1["name"])
# d1["age"] = 32
# print(d1)


d2 = dict(name="Mangesh", age=32, country="India")
print(d2)
print(d2["name"])
print(d2.get("country"))
# If key (country101) is not present, second param will reply
print(d2.get("country101", "does not exist"))

d2["name"] = "My friend"

for key, val in d2.items():  # d2.items() returns dic as tuple (key, value)
    print(key, val)
