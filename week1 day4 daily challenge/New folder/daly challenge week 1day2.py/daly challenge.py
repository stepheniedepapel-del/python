from datetime import datetime

def is_leap_year(year):
    """Check if a year is a leap year"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(birthdate):
    """Calculate age from birthdate"""
    today = datetime.now()
    age = today.year - birthdate.year
    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

def draw_cake(candles):
    """Draw the birthday cake with specified number of candles"""
    # Build the candle line with 'i' characters
    candle_line = "       ___" + "i" * candles + "___"
    
    cake = f"""
{candle_line}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""
    return cake

# Main program
print("🎂 Birthday Cake Generator 🎂")
print("=" * 40)

# Get birthdate from user
while True:
    try:
        birthdate_str = input("Please enter your birthdate (DD/MM/YYYY): ")
        birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
        break
    except ValueError:
        print("Invalid format! Please use DD/MM/YYYY (e.g., 25/12/1990)")

# Calculate age
age = calculate_age(birthdate)

# Get last digit of age for candles
candles = age % 10
if candles == 0:
    candles = 10  # If age ends in 0, show 10 candles

print(f"\n🎉 You are {age} years old!")
print(f"🕯️  Candles on your cake: {candles}")

# Check for leap year
leap_year = is_leap_year(birthdate.year)

if leap_year:
    print(f"\n✨ You were born in a leap year ({birthdate.year})!")
    print("That means you get TWO cakes!\n")
    print(draw_cake(candles))
    print("\n" + "=" * 30 + " CAKE #2 " + "=" * 30)
    print(draw_cake(candles))
else:
    print(f"\nYou were born in {birthdate.year}.")
    print(draw_cake(candles))

print("\n🎈 Happy Birthday! 🎈")