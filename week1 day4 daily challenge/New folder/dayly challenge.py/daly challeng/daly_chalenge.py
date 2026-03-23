import random


user_string = input("Please enter a string (exactly 10 characters): ")



if string_length < 10:
    print("String not long enough.")
    
    print("Perfect string")
    

    first_char = user_string[0]
    last_char = user_string[-1]
    print(f"First character: {first_char}")
    print(f"Last character: {last_char}")
    
    
    print("\nBuilding the string character by character:")
    built_string = ""
    for char in user_string:
        built_string += char
        print(built_string)
    
    
    print("\nBonus - Jumbled version:")
    char_list = list(user_string)  
    random.shuffle(char_list)      
    jumbled_string = "".join(char_list)  
    print(jumbled_string)