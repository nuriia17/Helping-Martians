import random

box_locations = [1, 2, 3]
box_weights =
print("Find all 3 boxes")
print("Enter the correct kilometers where the boxes are hidden.")
print("If you're wrong, the boxes will move to new locations.\n")

while True:
    guess1 = int(input("Enter the first location: "))
    guess2 = int(input("Enter the second location: "))
    guess3 = int(input("Enter the third location: "))


    if sorted([guess1, guess2, guess3]) == sorted(box_locations):
        print("\nCongratulations! You found all the boxes.")
        break
    else:
        print("\nWrong locations! The boxes moved to new places.")
        box_locations = random.sample(range(1, 9), 3)
print("Goodbye")