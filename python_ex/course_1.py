"""
# python list [Common & Mutable]
days = ["Mon", "Tue", "Wed", "Thur", "Fri"]

print(days)
print(days[0])
print(type(days))
print("Mon" in days)
print("len:", len(days))

days.reverse()
print(days)
"""

"""
# python tuple [Only Common operation]
days = ("Mon", "Tue", "Wed", "Thur", "Fri")
print(days)
print(days[0])
print(type(days))
"""


# python dictionary
jin_info = {
    "name" : "jin-young-do",
    "age" : 24,
    "korean" : True,
    "fav_food" : ["K-chicken_soup", "sushi", "chicken"]
}

print(jin_info)
jin_info["pet"] = True
print(jin_info)
print("name : ", jin_info["name"])
print("koren ? ",  jin_info["korean"])

jin_info.update(name="Chin-youngdo")
print(jin_info)
