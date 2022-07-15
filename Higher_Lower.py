# Author: Youngju Chae
# Higher or Lower Game

# Importing necessary modules
import random
from replit import clear
from art import logo_higher_lower
from game_data import data
from art import logo_versus

# Run the game
def higherLower():
  
  # Create necessary variables
  score = 0
  game_continue = True

  while game_continue:
    clear()
    print(logo_higher_lower)
    
    # Pick two categories
    copy_data = data
    category_a = random.choice(copy_data)
    copy_data.remove(category_a)
    
    category_b = random.choice(copy_data)
    copy_data.remove(category_b)

    if score > 0:
      print(f'Correct! Currect score: {score}')
      
    # Print decriptions of the two categories
    print(f"Compare Category A: {category_a['name']}, a {category_a['description']}, from {category_a['country']}")
    print(logo_versus)
    print()
    print(f"Category B: {category_b['name']}, a {category_b['description']}, from {category_b['country']}")

    # Determine player's choice
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    follower_a = category_a["follower_count"]
    follower_b = category_b["follower_count"]
    
    # Compare follower count and determine if player guesses correctly
    if follower_a > follower_b:
      if choice == 'a':
        score += 1
      else:
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")
        game_continue = False
    else:
      if choice == 'b':
        score += 1
      else:
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")
        game_continue = False

# Determine if player wants to play again
while(input("Do you want to play higher or lower game again? y or n: ") == 'y'):
  higherLower()
