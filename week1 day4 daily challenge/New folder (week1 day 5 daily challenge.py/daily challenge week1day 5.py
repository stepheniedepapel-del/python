# ============================================
# DAILY CHALLENGE SOLUTIONS
# ============================================

# ============================================
# CHALLENGE 1: SORTING WORDS
# ============================================

def sort_words():
    """
    Takes a comma-separated string of words and returns them sorted alphabetically.
    """
    # Step 1: Get Input
    user_input = input("Enter words separated by commas: ")
    
    # Step 2: Split the String into a list
    words_list = user_input.split(",")
    
    # Step 3: Sort the List (alphabetically)
    words_list.sort()
    
    # Step 4: Join the Sorted List back into a string
    sorted_string = ",".join(words_list)
    
    # Step 5: Print the Result
    print(sorted_string)
    return sorted_string


# ============================================
# CHALLENGE 2: LONGEST WORD
# ============================================

def longest_word(sentence):
    """
    Takes a sentence and returns the longest word.
    If multiple words have the same max length, returns the first one encountered.
    Punctuation is considered part of the word.
    """
    # Step 2: Split the Sentence into Words
    words = sentence.split()
    
    # Step 3: Initialize Variables
    longest = ""
    max_length = 0
    
    # Step 4: Iterate Through the Words
    for word in words:
        # Step 5: Compare Word Lengths
        if len(word) > max_length:
            longest = word
            max_length = len(word)
    
    # Step 6: Return the Longest Word
    return longest


# ============================================
# TESTING THE SOLUTIONS
# ============================================

print("=" * 50)
print("CHALLENGE 1: SORTING WORDS")
print("=" * 50)

# Test Challenge 1
print("\n--- Test Case 1 ---")
# Simulating input: "without,hello,bag,world"
test_input1 = "without,hello,bag,world"
words = test_input1.split(",")
words.sort()
result1 = ",".join(words)
print(f"Input: {test_input1}")
print(f"Output: {result1}")  # Expected: bag,hello,without,world

print("\n--- Test Case 2 ---")
test_input2 = "apple,banana,cherry"
words2 = test_input2.split(",")
words2.sort()
result2 = ",".join(words2)
print(f"Input: {test_input2}")
print(f"Output: {result2}")  # Expected: apple,banana,cherry

print("\n" + "=" * 50)
print("CHALLENGE 2: LONGEST WORD")
print("=" * 50)

# Test Challenge 2
test_cases = [
    "Margaret's toy is a pretty doll.",
    "A thing of beauty is a joy forever.",
    "Forgetfulness is by all means powerless!"
]

for i, test in enumerate(test_cases, 1):
    result = longest_word(test)
    print(f"\n--- Test Case {i} ---")
    print(f"Input: \"{test}\"")
    print(f"Output: \"{result}\"")

print("\n" + "=" * 50)
print("ALL TESTS COMPLETED!")
print("=" * 50)