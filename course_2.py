# function
"""
def say_hello(name):
    print("hello " + name + "!")

say_hello("jin-youngdo")

def minus(a, b=1):
    print(a-b)

# minus()함수의 argument인 b를 전달하지 않았지만
# b의 값이 1로 초기화 되어 있으므로 에러 x
minus(3)
"""

"""
# return formmat
def say_hello(name, age):
    return f"Hello {name} you are {age} years old"

hello = say_hello(age=24, name="Jin-youngdo")

print(hello)
"""

# Assignment Weeks_2
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def is_on_list(days, Wed) :
    if Wed in days :
        return True
    else : 
        return False

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

def get_x(days, index) :
    return days[index]

print("The fourth item in 'days' is:", get_x(days, 3))

def add_x(days, append_element) :
    days.append(append_element)

add_x(days, "Sat")
print(days)

def remove_x(days, remove_element) :
    days.remove(remove_element)

remove_x(days, "Mon")
print(days)
