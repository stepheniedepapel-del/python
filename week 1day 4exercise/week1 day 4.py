


def display_message():
    print("I am learning about functions in Python!")
def favorite_book(title):
    print(f"One of my favorite books is {title}")

def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")


import random

def compare_numbers(user_number):
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")


def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")


magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = magicians[i] + " the Great"


def get_random_temp():
    return random.randint(-10, 40)

def main_temp():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif 16 < temp <= 23:
        print("Nice weather.")
    elif 24 <= temp <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")


print("=" * 50)
print("EXERCISE 1")
print("=" * 50)
display_message()

print("\n" + "=" * 50)
print("EXERCISE 2")
print("=" * 50)
favorite_book("Alice in Wonderland")

print("\n" + "=" * 50)
print("EXERCISE 3")
print("=" * 50)
describe_city("Reykjavik", "Iceland")
describe_city("Paris")

print("\n" + "=" * 50)
print("EXERCISE 4")
print("=" * 50)
compare_numbers(50)

print("\n" + "=" * 50)
print("EXERCISE 5")
print("=" * 50)
make_shirt()
make_shirt(size="medium")
make_shirt(size="small", text="Hello!")

print("\n" + "=" * 50)
print("EXERCISE 6")
print("=" * 50)
make_great(magician_names)
show_magicians(magician_names)

print("\n" + "=" * 50)
print("EXERCISE 7")
print("=" * 50)
main_temp()