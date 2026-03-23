# Hangman Game - A fun word guessing game where you try to guess a hidden word by suggesting letters.
# Topics: Conditionals, Loops, Functions, Modules (random)

import random

# Word list provided in the assignment
WORDSLIST = ['correction', 'childish', 'beach', 'python', 'assertive', 
             'interference', 'complete', 'share', 'credit card', 'rush', 'south']

# ASCII art for hangman stages (0 wrong guesses to 6 wrong guesses)
HANGMAN_STAGES = [
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========='''
]

def get_random_word():
    """Select and return a random word from the word list."""
    return random.choice(WORDSLIST)

def display_hangman(wrong_attempts):
    """Display the current hangman ASCII art based on number of wrong attempts."""
    print(HANGMAN_STAGES[wrong_attempts])

def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed and unguessed letters as stars."""
    display = ""
    for char in word:
        if char == " ":
            display += "   "
        elif char.lower() in guessed_letters:
            display += f" {char.upper()} "
        else:
            display += " * "
    return display

def display_guessed_letters(guessed_letters):
    """Display all letters that have been guessed so far."""
    if guessed_letters:
        print(f"\n📋 Letters guessed: {', '.join(sorted(guessed_letters)).upper()}")

def get_player_guess(guessed_letters):
    """Get a valid letter guess from the player."""
    while True:
        guess = input("\n🔤 Guess a letter: ").strip().lower()
        if len(guess) != 1:
            print("❌ Please enter exactly one letter!")
            continue
        if not guess.isalpha():
            print("❌ Please enter a letter (A-Z) only!")
            continue
        if guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess.upper()}'! Try a different letter.")
            continue
        return guess

def check_win(word, guessed_letters):
    """Check if the player has guessed all letters in the word."""
    for char in word:
        if char != " " and char.lower() not in guessed_letters:
            return False
    return True

def play_round():
    """Play one round of Hangman. Returns True if player won, False if player lost."""
    word = get_random_word()
    guessed_letters = set()
    wrong_attempts = 0
    max_attempts = 6
    
    print("\n" + "=" * 50)
    print("🎮 HANGMAN GAME STARTED!")
    print("=" * 50)
    print(f"\n💡 The word has {len([c for c in word if c != ' '])} letters")
    print(f"💡 You have {max_attempts} attempts to guess the word")
    
    while wrong_attempts < max_attempts:
        print("\n" + "-" * 50)
        display_hangman(wrong_attempts)
        print(f"\n❤️  Attempts remaining: {max_attempts - wrong_attempts}")
        print(f"🔍 Word: {display_word(word, guessed_letters)}")
        display_guessed_letters(guessed_letters)
        
        guess = get_player_guess(guessed_letters)
        guessed_letters.add(guess)
        
        if guess in word.lower():
            print(f"✅ Good job! '{guess.upper()}' is in the word!")
            if check_win(word, guessed_letters):
                print("\n" + "=" * 50)
                display_hangman(wrong_attempts)
                print(f"\n🔍 Word: {display_word(word, guessed_letters)}")
                print(f"\n🎉 CONGRATULATIONS! You guessed the word: {word.upper()}!")
                print("=" * 50)
                return True
        else:
            wrong_attempts += 1
            print(f"❌ Sorry, '{guess.upper()}' is not in the word.")
            if wrong_attempts >= max_attempts:
                print("\n" + "=" * 50)
                display_hangman(wrong_attempts)
                print(f"\n💀 GAME OVER! The word was: {word.upper()}")
                print("=" * 50)
                return False

def play():
    """Main game function with replay option."""
    print("=" * 50)
    print("🎯 WELCOME TO HANGMAN!")
    print("=" * 50)
    print("\n📜 Rules:")
    print("   • Guess the hidden word one letter at a time")
    print("   • You have 6 attempts (head, body, 2 arms, 2 legs)")
    print("   • Don't guess the same letter twice!")
    print("   • Spaces in phrases are shown automatically")
    
    games_played = 0
    games_won = 0
    
    while True:
        won = play_round()
        games_played += 1
        if won:
            games_won += 1
        
        print(f"\n📊 Stats: {games_won}/{games_played} games won")
        print("\n" + "-" * 50)
        again = input("🔄 Play again? (yes/no): ").strip().lower()
        
        if again not in ['yes', 'y']:
            print("\n" + "=" * 50)
            print(f"👋 Thanks for playing! Final score: {games_won}/{games_played}")
            print("=" * 50)
            break

if __name__ == "__main__":
    play()