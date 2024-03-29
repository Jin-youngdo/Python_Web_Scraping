# 조건문
"""
def age_check(age):
    print(f"you are {age}years old")

    if age<18:
        print("you cant drink")
    elif age==18 or age==19:
        print("you are new to this!")
    elif age>20 and age<25:
        print("you are still kind of young")
    else:
        print("enjoy your drink")


age_check(23)
"""

# 반복문
"""
days = ("Mon", "Tue", "Wed", "Thur", "Fri")

for i in days:
    if i == "Wed":
        break
    else:
        print(i)

for i in "Jin-youngdo":
    print(i)
"""

# Assignment Weeks_3
"""
Again, the code is broken, you need to create 4 functions.
  - add_to_dict: Add a word to a dict.
  - get_from_dict: Get a word from inside a dict.
  - update_word: Update a word inside of the dict.
  - delete_from_dict: Delete a word from the dict.

All this functions should check for errors, follow the comments to see all cases you need to cover.

There should be NO ERRORS from Python in the console.
"""
"""
def add_to_dict(dic, key, value=""):
  dic_type = type(dic)   
  key_type = type(key)

  if dic_type!=dict:
    print(f"You need to send a dictionary. You sent: {dic_type}")
  elif key in dic:
    print(f"{key} is already on the dictionary. Won't add")
  elif dic_type==dict and key_type==str:
    if value=="":
        print("You need to send a word and a definition")
    else:
        print(f"{key} has been added.")
        dic[f"{key}"] = value

def get_from_dict(dic, key=""):
  if type(dic)!=dict:
    print(f"You need to send a dictionary. You sent: {type(dic)}")
  elif key=="":
    print("You need to send a word to search for")
  elif key not in dic:
    print(f"{key} was not found in this dict")
  elif key in dic:
    print(f"{key}: {dic.get(key)}")

def update_word(dic, key="", value=""):
  if type(dic)!=dict:
    print(f"You need to send a dictionary. You sent: {type(dic)}")
  elif value=="":
    print("You need to send a word and a definition to update.")
  elif key not in dic:
    print(f"{key} is not on the dict. Can't update non-existing word.")
  else:
    dic_2 = {key : value}
    dic.update(dic_2)
    print(f"{key} has been updated to: {value}")

def delete_from_dict(dic, key=""):
  if type(dic)!=dict:
    print(f"You need to send a dictionary. You sent: {type(dic)}")
  elif key=="":
    print("You need to specify a word to delete")
  elif key not in dic:
    print(f"{key} is not in this dict. Won't delete")
  elif key in dic:
    del dic[key]
    print(f"{key} has been deleted")

# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/

import os

os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

# \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/
"""